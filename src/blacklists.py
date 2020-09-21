import boto3
from boto3.dynamodb.conditions import Key

class Blacklists():
    def __init__(self):
        self.ddb = boto3.resource('dynamodb')
        self.table = self.ddb.Table('Blacklists')

    def is_blacklisted(self, word):
        key_name = 'name'
        index_name = 'nameGSI'

        key_condition = Key(key_name).eq(word)

        try:
            response = self.table.query(
                IndexName=index_name,
                KeyConditionExpression=key_condition
            )
        except Exception as e:
            print(e)
            raise

        data = response['Items']
        # Get next page
        while 'LastEvaluatedKey' in response:
            print('=== Paginated ===')
            response = self.table.query(
                IndexName=index_name,
                KeyConditionExpression=key_condition,
                ExclusiveStartKey=response['LastEvaluatedKey']
            )
            data.extend(response['Items'])
        
        if len(data) > 0:
            return True
        else:
            return False

    def add_blacklist(self):
        pass