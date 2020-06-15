import boto3
import json
#import create_playlist_table
#import insert_playlist
#import get_playlist
import list_playlists


def lambda_handler(event, context):
    #response = insert_playlist.insert(event['body'])
    response = list_playlists.list()
    return {
        'statusCode': 200,
        'body': response
    }
