from dataclasses import dataclass
import psycopg2
from psycopg2.extras import RealDictCursor
import json
import boto3
from botocore.exceptions import ClientError


def get_credentials():

    secret_name = "db_credentials"
    region_name = "ap-south-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']
    return json.loads(secret)

    # Your code goes here.

credentials = get_credentials()

conn = psycopg2.connect(
    host =      "dbhost.region.rds.amazonaws.com",
    database =  "dbname",
    user =      credentials['username'],
    password =  credentials['password']
)

def lambda_handler(event, context):
    cur = conn.cursor(cursor_factory = RealDictCursor)
    cur.execute("select * from users limit 10")
    results = cur.fetchall()
    json_result = json.dumps(results)
    print(json_result)
    cur.close()
    return json_result
    
