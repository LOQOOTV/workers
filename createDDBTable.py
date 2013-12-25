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

	def createTable( self, keyName, keyType, rangeName=None, rangeType=None, tableName ):
		message_table_schema = co.create_schema(
        	hash_key_name=keyName,
        	hash_key_proto_value=keyType,
        	range_key_name=rangeName,
        	range_key_proto_value=rangeType
    )
		table = conn.create_table(
        	name= tableName,
        	schema=message_table_schema,
        	read_units=5,
        	write_units=10
    )
