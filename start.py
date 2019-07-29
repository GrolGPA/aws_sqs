import boto3
import boto3.session
import threading
from . import config

def list():

    try:

        sqs = boto3.Session(
            aws_access_key_id=config.Credentials.aws_key_id,
            aws_secret_access_key=config.Credentials.aws_access_key,
            region_name='eu-west-1'
        ).resource('sqs')


        queue_url = 'SQS_QUEUE_URL'

        # List SQS queues
        response = sqs.list_queues()

        print(response['QueueUrls'])


    except:

        return { "message" : "Listing failed" }



# response = sqs.create_queue(
        #     QueueName='TEST_SQS_QUEUE',
        #     Attributes={
        #         'Atribut_1': 'test1',
        #         'Atribut_2': 'test2'
        #     }
        # )



# TODO : 1) Poll from an aws sqs queue
# TODO : 2) Get a message
# TODO : 3) Simulate to launch a background process (for example sleep 1 minute)
# TODO : 4) Keep increasing message visibility to prevent task to return to sqs
# TODO : 5) When finished the background process then consume the message from sqs0