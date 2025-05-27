# scripts/upload_to_s3.py
import boto3

BUCKET_NAME = "etl-educacao"
LOCAL_FILE = "./data/raw/microdados_censo_escolar_2024/dados/microdados_ed_basica_2024.csv"
S3_KEY = "raw/microdados_ed_basica_2024.csv"

s3 = boto3.client("s3")
s3.upload_file(LOCAL_FILE, BUCKET_NAME, S3_KEY)

print("Upload realizado com sucesso!")
