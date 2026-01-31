import os

AWS_REGION = os.getenv("AWS_REGION", "us-east-1")
AWS_ENDPOINT_URL = os.getenv("AWS_ENDPOINT_URL", "http://localstack:4566")

SQS_QUEUE_NAME = "summary-jobs"
DYNAMODB_TABLE = "summary_jobs"
