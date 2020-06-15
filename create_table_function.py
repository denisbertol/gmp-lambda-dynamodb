"""
Your module description
"""
import boto3

def create(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.client('dynamodb')

    table_name = 'playlist'

    response = dynamodb.list_tables()

    if table_name not in response['TableNames']:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[
                {
                    'AttributeName': 'id_playlist',
                    'KeyType': 'HASH'  # Partition key
                }
            ],
            AttributeDefinitions=[
                {
                    'AttributeName': 'id_playlist',
                    'AttributeType': 'S'
                },

            ],
            ProvisionedThroughput={
                'ReadCapacityUnits': 5,
                'WriteCapacityUnits': 5
            }
        )
        # Wait until the table exists.
        dynamodb.get_waiter('table_exists').wait(TableName=table_name)
        response = dynamodb.describe_table(TableName=table_name)
        if response["Table"]['TableStatus'] == 'ACTIVE':
            print("Tabela " + table_name + " criada com sucesso")
    else:
        print("Tabela " + table_name + " ja existe")