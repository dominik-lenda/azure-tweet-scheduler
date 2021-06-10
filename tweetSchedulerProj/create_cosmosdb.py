from azure.cosmos import CosmosClient, PartitionKey, exceptions

import os

url = os.environ['ACCOUNT_URI']
key = os.environ['ACCOUNT_KEY']
client = CosmosClient(url, credential=key)

database_name = 'tweetSchedulerDB'
try:
    database = client.create_database(database_name)
except exceptions.CosmosResourceExistsError:
    database = client.get_database_client(database_name)
container_name = 'Tweets'

try:
    container = database.create_container(id=container_name, partition_key=PartitionKey(path="/productName"))
except exceptions.CosmosResourceExistsError:
    container = database.get_container_client(container_name)
except exceptions.CosmosHttpResponseError:
    raise

container.upsert_item({
    'id': '1',
    'tweet_content': 'First tweet'
    }
)