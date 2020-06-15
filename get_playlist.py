import os
import json
import boto3
import decimalencoder

def get(id_playlist,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')
        
    table = dynamodb.Table('playlist')

    # fetch todo from the database
    result = table.get_item(
        Key={
            'id_playlist': id_playlist
        }
    )

    return json.dumps(result['Item'],cls=decimalencoder.DecimalEncoder)