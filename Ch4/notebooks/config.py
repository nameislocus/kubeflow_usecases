import os

S3_END_POINT = os.getenv('S3_END_POINT', 'http://minio-kubeflow.apps.openmaru.ocp482.com')
S3_ACCESS_ID = os.getenv('AWS_ACCESS_KEY_ID', 'minio')
S3_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY', 'minio123')

BASE_IMAGE = 'docker.io/pytorch/pytorch:1.0-cuda10.0-cudnn7-runtime'
BUCKET_NAME = 'opf-datacatalog'
