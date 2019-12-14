import os
from azure.servicebus.control_client import ServiceBusService, Message, Topic
#from pymongo import MOngoClient
#connection_str = os.environ['SB_CONN_STR']
#mongo_conn_str = os.environ['PROD_MONGODB']
bus_service = ServiceBusService(
    service_namespace="cpsc-topic.servicebus.windows.net", shared_access_key_name="RootManageSharedAccessKey", shared_access_key_value="FG76GE6eVG0HfdRFp9d7+opJMp4qhluotQIxAVpGmEw=")
topic_name = "on-prem-test"  # the topic name already defined in azure
subscription = "heroku_consumer"  # unique name for this application/consumer
bus_service.create_topic(topic_name)
# create subscription
bus_service.create_subscription(topic_name, subscription)

# get subscription message
msg = bus_service.receive_subscription_message(
    topic_name, subscription, peek_lock=True)
print(msg.body)
# write to DB
#mClient = MongoClient(mongo_conn_str)
# get db
msg.complete()
