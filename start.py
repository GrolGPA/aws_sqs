import boto3
import boto3.session
import threading


sqs = boto3.client('sqs')

# List SQS queues
response = sqs.list_queues()
print(response['QueueUrls'])

response = sqs.create_queue(
    QueueName='TEST_SQS_QUEUE',
    Attributes={
        'Atribut_1': 'test1',
        'Atribut_2': 'test2'
    }
)

print(response['QueueUrl'])
