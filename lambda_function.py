import boto3

def lambda_handler(event, context):
    s3 = boto3.client('s3')
    sns = boto3.client('sns', region_name='ap-south-1')
    
    source_bucket = 'disaster-primary-mumbai'
    dest_bucket = 'disaster-backup-singapore'
    sns_topic = 'arn:aws:sns:ap-south-1:891612580748:disaster-recovery-alert'
    
    file_name = event['Records'][0]['s3']['object']['key']
    
    s3.copy_object(
        CopySource={'Bucket': source_bucket, 'Key': file_name},
        Bucket=dest_bucket,
        Key=file_name
    )
    
    sns.publish(
        TopicArn=sns_topic,
        Message=f'Backup Complete! File "{file_name}" copied to Singapore!',
        Subject='CloudGuard — Disaster Recovery Alert'
    )
    
    return {
        'statusCode': 200,
        'body': 'Backup Successful!'
    }