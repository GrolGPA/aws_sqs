#!/usr/bin/python3

from time import sleep
from sqs import SQS
import argparse

# Before starting need copy ".env.sample" file to ".env" and write AWS credentials in it


def main():
    try:

        sqs = SQS()
        sqs.pool()  # If not set queue name will be use the default name - "TEST_QUEUE"
        sqs.send_message("TEST 222")    # You can set message body or message will be create with the default message body


        i = 1
        # while True:
        while i < 20:

            # Printing messages
            print(sqs.get_queues())

            i += 1

            # Starting background process after printing first message
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