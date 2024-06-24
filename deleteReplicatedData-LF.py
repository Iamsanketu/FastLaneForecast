import boto3
import json

# Initialize the S3 client
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    
    # Extract source bucket and object key from the event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    object_key = event['Records'][0]['s3']['object']['key']
    
    # Extract file name without extension
    target_file_name = object_key[:-5]
    
    # Define the target buckets and object keys
    target_bucket_1 = 'replicated-data-bucket'
    object_key_1 = f"{target_file_name}.json"
    
    target_bucket_2 = 'transformed-csv-data-bucket'
    object_key_2 = f"{target_file_name}.csv"
    
    # Delete the object from the target buckets
    s3_client.delete_object(Bucket=target_bucket_1, Key=object_key_1)
    print(f'Data deleted successfully from {target_bucket_1}')
    
    s3_client.delete_object(Bucket=target_bucket_2, Key=object_key_2)
    print(f'Data deleted successfully from {target_bucket_2}')
    
    return {
        'statusCode': 200,
        'body': json.dumps('Data deleted successfully from the target buckets')
    }
    