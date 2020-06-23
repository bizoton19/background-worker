import os
import requests
from pymongo import MongoClient
import json
import pprint
import datetime


def update_job_history():
    result = db.job_history.find_one({'job_name':'recalls_to_mongodb'})
    result['run_date'] = datetime.datetime.today()
    result['collection_size'] = db.recalls.count_documents({})
    result['db_size']=db.command('dbstats')['dataSize']
    db.job_history.replace_one({'_id': result['_id']},result)
    mClient.close()

def get_recalls_api_data(url,start_date):
    payload= {'RecallDateStart':start_date,'format':'json'}
    r = requests.get(url,params=payload)
    print(r)
      
    if  r.status_code > 200:
        print('Error Retreiving recall')
        print(r.status_code)
        #sendEmail
        exit()
    else:
       
        print('done reading from api')
        return r.json()
        

def load_recalls_data(msg_body):
    mClient = MongoClient(mongo_conn_str)
    try:
        
        db = mClient.neiss_test
        print('about to bulk insert into mongo')
        result = db.recalls.insert(msg_body)
        print('done inserting into mongo')
        print('updating job history')
        update_job_history()
       
    except Exception as err:
        print(err) 
    finally:
        print('Process completed')
        mClient.close()

def get_recall_run_date() :
    try:
        # write to DB
        mClient = MongoClient(mongo_conn_str)
        # get db
        db = mClient.neiss_test
        result = db.job_history.find_one({'job_name':'recalls_to_mongodb'})
        pprint.pprint(result)
        print(result['run_date'])
           
    except Exception as err:
        #msg.unlock()  # call this method if any of the database operation above fail
        print(err)
    finally:
        mClient.close()
        return result['run_date'] 

mongo_conn_str = os.getenv('PROD_MONGODB')
mClient = MongoClient(mongo_conn_str)
db = mClient.neiss_test

SERVICE_ROOT = "https://www.saferproducts.gov/RestWebServices/Recall" 

last_run_date =get_recall_run_date()
today = last_run_date.strftime("%Y-%m-%d")
if datetime.datetime.today() > last_run_date:
   data = get_recalls_api_data(SERVICE_ROOT,today)
   load_recalls_data(data)



    

