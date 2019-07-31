#!/usr/bin/python3

import boto3
import os
from dotenv import load_dotenv
from time import sleep
import argparse

def get_client():
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


        sqs = get_client()

        queue_url = pool(sqs)

        i = 1
        while True:

            print(get_queues(sqs, queue_url))
            i += 1
            if i == 2:

                print ("Pause for 1 minute")

                t = 1
                while t < 5:

                    print ('.', sep=' ', end='', flush=True)
                    t = t + 1
                    sleep(1)
                print ("\nPause ended")


    except:

        return {"message": "Some error"}

if __name__ == '__main__':
    main()



# TODO : 1) Poll from an aws sqs queue
# TODO : 2) Get a message
# TODO : 3) Simulate to launch a background process (for example sleep 1 minute)
# TODO : 4) Keep increasing message visibility to prevent task to return to sqs
# TODO : 5) When finished the background process then consume the message from sqs0