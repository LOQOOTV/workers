#!/usr/bin/env python

import boto.dynamodb2
from boto.dynamodb2.fields import HashKey, RangeKey, KeysOnlyIndex, AllIndex
from boto.dynamodb2.table import Table
from boto.dynamodb2.types import NUMBER

AWS_SECERT_KEY = os.environ['AWS_SECERT_ACCESS_KEY']
AWS_ACCESS_KEY_ID =  os.environ['AWS_ACCESS_KEY_ID']

conn = boto.dynamodb.connect_to_region(
        'us-west-2',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECERT_ACCESS_KEY)

class DynamoDB ():


	def createTable( self, tableName, hashKeyName, hashKeyType, rangeKeyName=None, rangeKeyType=None, 	 ):
    		Table.create(tableName, schema=[
			HashKey(hashKeyName, data_type = hashKeyType),
			RangeKey(rangeKeyName, data_type = rangeKeyType)],
			throughput{
				'read': 5,
				'write': 10,
				},
			indexes=[

					]
