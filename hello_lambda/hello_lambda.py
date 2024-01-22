"""
A Lambda Function to Greet Hello, <User>. The code is a simplified version of the official example below

Source: https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-create-api-as-simple-proxy-for-lambda.html
"""

import json

def lambda_handler(event, context):
    """
    event argument needs to be in the fasion `{"greeter": "Senthil"}`
    context argument is a default passed to the handler function. Know more here: https://docs.aws.amazon.com/lambda/latest/dg/python-context.html
    """
    greeter = event['greeter']

    res = {
    'statusCode': 200,
    'headers': {
        'Content-Type': '*/*'
    },
    'body': 'Hello everyone, This is '+greeter+'!'
    }
    return res