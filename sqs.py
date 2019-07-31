#!/usr/bin/python3

import boto3
import os
from dotenv import load_dotenv

class SQS():

    def __init__(self):

        try:

            # Loading credentials from the .env file
            load_dotenv('.env')


            self.sqs = boto3.client(
            'sqs',
            aws_access_key_id=os.environ.get('AWS_KEY_ID'),
            aws_secret_access_key=os.environ.get('AWS_ACCESS_KEY'),
            region_name=os.environ.get('REGION')
            )

        except:

            return {"message": "Connection failed"}


    def list(self):

        try:


            # List SQS queues
            response = self.sqs.list_queues()

            self.queues = response['QueueUrls']


        except:

            return { "message" : "Listing failed" }


    def pool(self, queue_name="TEST_QUEUE"):

        try:

            # Create a SQS queue with long polling enabled
            response = self.sqs.create_queue(
                QueueName=queue_name,
                Attributes={'ReceiveMessageWaitTimeSeconds': '20'}
            )

            self.queue_url = response['QueueUrl']

        except:

            return {"message" : "Pooling error"}


    def send_message(self, message_body="New test message"):
        try:

            # Sending test message
            response = self.sqs.send_message(
                QueueUrl=self.queue_url,
                MessageBody=message_body
            )

            print ("Sending message successful")
            return response

        except:

            return {"message" : "Sending error"}


    def get_queues(self):
        try:

            response = self.sqs.receive_message(
                QueueUrl=self.queue_url
            )

            return response

        except:

            return {"message" : "Getting error"}