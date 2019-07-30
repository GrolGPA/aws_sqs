#!/usr/bin/python3

import boto3
import boto3.session
import threading
from config import Credentials
import argparse

def session():
    try:

        sqs = boto3.client('sqs')
        # sqs = boto3.Session(
        #     aws_access_key_id=Credentials.aws_key_id,
        #     aws_secret_access_key=Credentials.aws_access_key,
        #     region_name='eu-west-1'
        # ).resource('sqs')


        return sqs

    except:

        return {"message": "Connection failed"}


def list(sqs):

    try:


        # List SQS queues
        response = sqs.list_queues()

        print(response['QueueUrls'])



    except:

        return { "message" : "Listing failed" }


def create(sqs):
    try:

        queue_url = 'SQS_QUEUE_URL'

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
        print (sqs)

        # response = create(sqs)
        # print(response)
        response = list(sqs)
        print(response)

    except:

        print(response)

if __name__ == '__main__':
    main()




# TODO : 1) Poll from an aws sqs queue
# TODO : 2) Get a message
# TODO : 3) Simulate to launch a background process (for example sleep 1 minute)
# TODO : 4) Keep increasing message visibility to prevent task to return to sqs
# TODO : 5) When finished the background process then consume the message from sqs0