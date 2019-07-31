#!/usr/bin/python3

import boto3
import threading
import os
from dotenv import load_dotenv
import argparse

def session():
    try:

        load_dotenv('.env')

        sqs = boto3.client(
        'sqs',
        aws_access_key_id=os.environ.get('AWS_KEY_ID'),
        aws_secret_access_key=os.environ.get('AWS_ACCESS_KEY'),
        region_name=os.environ.get('REGION')
        )

        return sqs

    except:

        return {"message": "Connection failed"}


def list(sqs):

    try:


        # List SQS queues
        response = sqs.list_queues()

        # return (response['QueueUrls'])
        return response


    except:

        return { "message" : "Listing failed" }


def create(sqs):

    try:

        # Create a SQS queue with long polling enabled
        response = sqs.create_queue(
            QueueName='SQS_QUEUE_NAME',
            Attributes={'ReceiveMessageWaitTimeSeconds': '20'}
        )

        return response['QueueUrl']

    except:

        return {"message" : "Pooling error"}


def send(sqs, url):
    try:

        queue_url = 'url'

        # Send message to SQS queue
        response = sqs.send_message(
            QueueUrl=queue_url,
            DelaySeconds=10,
            MessageAttributes={
                'Title': {
                    'DataType': 'String',
                    'StringValue': 'The Whistler'
                },
                'Author': {
                    'DataType': 'String',
                    'StringValue': 'John Grisham'
                },
                'WeeksOn': {
                    'DataType': 'Number',
                    'StringValue': '6'
                }
            },
            MessageBody=(
                'Information about current NY Times fiction bestseller for '
                'week of 12/11/2016.'
            )
        )

        return(response['MessageId'])

    except:

        return {"message" : "Sending error" }

def main():
    try:


        sqs = session()

        QueueUrl = create(sqs)
        print(QueueUrl)

        urls = list(sqs)
        print(urls)


        response = create(sqs, QueueUrl)
        print(response)
        #



    except:

        print("Error")

if __name__ == '__main__':
    main()



# TODO : 1) Poll from an aws sqs queue
# TODO : 2) Get a message
# TODO : 3) Simulate to launch a background process (for example sleep 1 minute)
# TODO : 4) Keep increasing message visibility to prevent task to return to sqs
# TODO : 5) When finished the background process then consume the message from sqs0