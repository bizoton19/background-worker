import os
from azure.servicebus.control_client import ServiceBusService, Message, Topic
from pymongo import MongoClient
import json

mongo_conn_str = os.getenv('PROD_MONGODB')
shared_access_key = os.getenv('shared_access_key')
shared_access_value = os.getenv('shared_access_value')
service_namespace = os.getenv('service_namespace')
print(service_namespace)

bus_service = ServiceBusService(service_namespace=service_namespace, shared_access_key_name=shared_access_key,
                                shared_access_key_value=shared_access_value)
topic_name = "on-prem-test"  # the topic name already defined in azure
subscription = "heroku_consumer"  # unique name for this application/consumer
bus_service.create_topic(topic_name)
# create subscription
bus_service.create_subscription(topic_name, subscription)

# get subscription message
msg = bus_service.receive_subscription_message(
    topic_name, subscription, peek_lock=False)
msg_body = None
entity = None
if msg.body is None:
    print('No messages to retrieve')
    exit()
else:
    msg_body = msg.body.decode("utf-8")
    entity = json.loads(msg_body)
    print(msg_body)

try:
    # write to DB
    mClient = MongoClient(mongo_conn_str)
    # get db
    db = mClient.neiss_test
    result = db.report.insert_one(entity)
    print('Created {0}'.format(result.inserted_id))
except Exception:
    msg.unlock()  # call this method if any of the database operation above fail
finally:
    print('Process completed')
