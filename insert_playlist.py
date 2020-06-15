"""
Your module description
"""

import boto3
import json
import uuid

def insert(playlist,dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('playlist')

    playlistItem = json.loads(playlist)    
    
    playlistItem["id_playlist"] = str(uuid.uuid1())
    
    table.put_item(Item=playlistItem)
    
    return json.dumps(playlistItem)