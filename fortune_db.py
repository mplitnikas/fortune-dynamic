#!/usr/bin/python
import random
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('fortunes')
current_key = 1

def put_item(text):
    global current_key
    table.put_item(
            Item={
                'key': current_key,
                'fortune': text
                }
            )
    current_key += 1

def get_item(num):
    return table.get_item(
            Key={
                'key': num
                }
            )

def get_fortune(num):
    return get_item(num).get('Item').get('fortune')

def get_random_fortune():
    return get_fortune(random.choice(range(318)))
