import time
import boto3
from app.core.config import AWS_REGION, AWS_ENDPOINT_URL, SQS_QUEUE_NAME
from app.services.storage_service import update_status

sqs = boto3.client(
    "sqs",
    region_name=AWS_REGION,
    endpoint_url=AWS_ENDPOINT_URL
)

def get_queue_url():
    response = sqs.create_queue(QueueName=SQS_QUEUE_NAME)
    return response["QueueUrl"]

def run():
    queue_url = get_queue_url()
    print("Worker listening...")

    while True:
        messages = sqs.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=1,
            WaitTimeSeconds=10
        ).get("Messages", [])

        for msg in messages:
            job_id = msg["Body"]
            print(f"Processing job {job_id}")

            update_status(job_id, "PROCESSING")
            time.sleep(3)
            update_status(job_id, "COMPLETED")

            sqs.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=msg["ReceiptHandle"]
            )

if __name__ == "__main__":
    run()