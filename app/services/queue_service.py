import boto3
from app.core.config import AWS_REGION, AWS_ENDPOINT_URL, SQS_QUEUE_NAME

sqs = boto3.client(
    "sqs",
    region_name=AWS_REGION,
    endpoint_url=AWS_ENDPOINT_URL
)

def get_queue_url():
    response = sqs.create.queue(QueueName=SQS_QUEUE_NAME)
    return response["QueueUrl"]

def send_job(job_id: str):
    queue_url = get_queue_url()
    sqs.send_message(
        QueueUrl=queue_url,
        MessageBody=job_id
    )