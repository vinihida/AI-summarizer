import boto3
from datetime import datetime
from app.core.config import AWS_REGION, AWS_ENDPOINT_URL, DYNAMODB_TABLE

dynamodb = boto3.resource(
    "dynamodb",
    region_name=AWS_REGION,
    endpoint_url=AWS_ENDPOINT_URL
)

def get_table():
    existing_tables = dynamodb.meta.client.list_tables()["TableNames"]

    if DYNAMODB_TABLE not in existing_tables:
        dynamodb.create_table(
            TableName=DYNAMODB_TABLE,
            KeySchema=[{"AttributeName": "job_id", "KeyType": "HASH"}],
            AttributeDefinitions=[{"AttributeName": "job_id", "AttributeType": "S"}],
            BillingMode="PAY_PER_REQUEST"
        )

    return dynamodb.Table(DYNAMODB_TABLE)

def save_job(job_id: str, status: str):
    table = get_table()
    table.put_item(
        Item={
            "job_id": job_id,
            "status": status,
            "created_at": datetime.utcnow().isoformat()
        }
    )

def update_status(job_id: str, status: str):
    table = get_table()
    table.update_item(
        Key={"job_id": job_id},
        UpdateExpression="SET #s = :s",
        ExpressionAttributeNames={"#s": "status"},
        ExpressionAttributeValues={":s": status}
    )

def get_job(job_id: str):
    table = get_table()
    response = table.get_item(Key={"job_id": job_id})
    return response.get("Item")
