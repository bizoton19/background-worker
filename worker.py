import os
from azure.servicebus import ServiceBusClient
#from pymongo import MOngoClient
connection_str =  os.environ['SB_CONN_STR']
mongo_conn_str = os.environ['PROD_MONGODB']
sb_client = ServiceBusClient.from_connection_string(connection_str)
topic_name = "on-prem-test" #the topic name already defined in azure
subscription = "heroku_consumer" #unique name for this application/consumer
sb_client.create_topic(topic_name)

#get topic
topic_client = sb_client.get_topic(topic_name)

#create subscription
sb_client.create_subscription(topic_name, subscription)

#get subscription message
msg = bus_service.receive_subscription_message(topic_name, subscription, peek_lock=True)
print(msg.body)
 #write to DB
 #mClient = MongoClient(mongo_conn_str)
#get db 
#db = mClient.

msg.complete()