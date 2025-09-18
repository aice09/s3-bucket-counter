# S3 Object Counter

⚡ Fast multithreaded object counter for **AWS S3** and **S3-compatible storage**  
(MinIO, Ceph, Scality, etc) using [boto3](https://boto3.amazonaws.com).

Traditional `aws s3 ls --recursive` can be slow or timeout for **millions of objects**.  
This tool counts objects efficiently using **parallel API calls**.

---

## 🚀 Features
- Counts total objects in a bucket
- Uses **parallel threads** for high performance
- Works with AWS and on-prem S3 backends (MinIO, Ceph, etc)
- Simple, self-contained script

---

## 📦 Installation

Clone the repo:
```bash
git clone https://github.com/<your-username>/s3-object-counter.git
cd s3-object-counter
```
## Create a virtual environment (recommended):
```
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

## ⚙️ Usage

Set your environment variables:

```
export S3_ENDPOINT="https://your-s3-endpoint"
export AWS_ACCESS_KEY_ID="your-access-key"
export AWS_SECRET_ACCESS_KEY="your-secret-key"
export S3_BUCKET="your-bucket"
export MAX_WORKERS=20   # optional, default = 10
```

Run the script:

```
python counter.py
```
Example output:

```
✅ Total objects in bucket 'my-bucket': 12,345,678
```

## 🛠 Notes
- Requires only list permission (s3:ListBucket)
- Adjust MAX_WORKERS depending on backend performance
- For huge buckets (10M+ objects), parallel mode makes a big difference
