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


def pool(sqs):

    try:

        # Create a SQS queue with long polling enabled
        response = sqs.create_queue(
            QueueName='SQS_TEST_QUEUE',
            Attributes={'ReceiveMessageWaitTimeSeconds': '20'}
        )

        return response['QueueUrl']

    except:

        return {"message" : "Pooling error"}


def send_message(sqs, queue_url):
    try:


        response = sqs.send_message(MessageBody='TEST message')

        return response

    except:

        return {"message" : "Sending error"}


def get_queues(sqs, queue_url):
    try:

        response = sqs.receive_message(
            QueueUrl=queue_url
        )

        # queue = sqs.get_queue_by_name(QueueName='SQS_TEST_QUEUE')
        #
        # queues = sqs.queues.all()

        # for queue in messages:
        #     print(queue.url)

        # print(queue.url)
        # print(queue.attributes.get('DelaySeconds'))

        return response

    except:

        return {"message" : "Getting error"}


def main():
    try:


        sqs = session()

        queue_url = pool(sqs)
        # print(queue_url)

        messages = get_queues(sqs, queue_url)
        print(messages)

        # queues = get_queues(sqs)
        # for i in response:
        #     print (response[i])


        # send_message(sqs, queue_url)



        # urls = list(sqs)
        # print(urls)

        # message = get_message(sqs,queue_url)



    except:

        print("Error")

if __name__ == '__main__':
    main()



# TODO : 1) Poll from an aws sqs queue
# TODO : 2) Get a message
# TODO : 3) Simulate to launch a background process (for example sleep 1 minute)
# TODO : 4) Keep increasing message visibility to prevent task to return to sqs
# TODO : 5) When finished the background process then consume the message from sqs0