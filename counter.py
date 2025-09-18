import boto3
from concurrent.futures import ThreadPoolExecutor, as_completed
import os

# ---- Configuration via ENV ----
S3_ENDPOINT = os.getenv("S3_ENDPOINT", "https://your-s3-endpoint")
ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID", "your-access-key")
SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY", "your-secret-key")
BUCKET_NAME = os.getenv("S3_BUCKET", "your-bucket")
MAX_WORKERS = int(os.getenv("MAX_WORKERS", "10"))  # default = 10 threads

# ---- Connect to S3 ----
s3 = boto3.client(
    "s3",
    endpoint_url=S3_ENDPOINT,
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY
)

# ---- Function to fetch one page ----
def fetch_page(continuation_token=None):
    if continuation_token:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME, ContinuationToken=continuation_token)
    else:
        response = s3.list_objects_v2(Bucket=BUCKET_NAME)

    count = len(response.get("Contents", []))
    next_token = response.get("NextContinuationToken")
    return count, next_token

# ---- Parallel counting ----
def count_objects():
    total_count = 0
    futures = []
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        count, token = fetch_page()
        total_count += count

        while token:
            futures.append(executor.submit(fetch_page, token))
            count, token = fetch_page(token)
            total_count += count

        for future in as_completed(futures):
            count, _ = future.result()
            total_count += count

    return total_count

if __name__ == "__main__":
    total = count_objects()
    print(f"✅ Total objects in bucket '{BUCKET_NAME}': {total}")
