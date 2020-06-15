import os
import json
import boto3
import decimalencoder


def list(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
        
    table = dynamodb.Table('playlist')

    # fetch all todos from the database
    result = table.scan()

    return json.dumps(result['Items'],cls=decimalencoder.DecimalEncoder)