import os
import time
from elasticsearch import Elasticsearch
import requests
from pymongo import MongoClient
import json
import pprint
import datetime
import fulltext 
from fulltext import mappings, mappings_index


def update_job_history(job_name):
    result = db.job_history.find_one({'job_name':job_name})
    result['run_date'] = datetime.datetime.today()
    result['collection_size'] = db.recalls.count_documents({})
    result['db_size']=db.command('dbstats')['dataSize']
    db.job_history.replace_one({'_id': result['_id']},result)
    mClient.close()

def get_recalls_api_data(url,start_date):
    payload= {'RecallDateStart':start_date,'format':'json'}
    r = requests.get(url,params=payload)
    
      
    if  r.status_code > 200:
        print('Error Retreiving recall')
        print(r.status_code)
        #sendEmail
        exit()
    else:
       
        print('done reading from api')
        return r
        

def load_recalls_data(msg_body):
    mClient = MongoClient(mongo_conn_str)
    try:
        
        db = mClient.neiss_test
        print('about to bulk insert into mongo')
        result = db.recalls.insert(msg_body)
        print('done inserting into mongo')
        print('updating job history')
        update_job_history(job_name="recalls_to_mongo")
       
    except Exception as err:
        print(err) 
    finally:
        print('Process completed')
        mClient.close()

def get_recall_run_date() :
    # write to DB
    mClient = MongoClient(mongo_conn_str)
    try:
        db = mClient.neiss_test
        result = db.job_history.find_one({'job_name':'recalls_to_mongodb'})
        pprint.pprint(result)
        print(result['run_date'])
        
        return result['run_date'] 
           
    except Exception as err:
        #msg.unlock()  # call this method if any of the database operation above fail
        print(err)
        
    finally:
        mClient.close()
        print("connection closed to mongo")
        
       

def index_recalls(data, index_name, delete_index=False):
    es = Elasticsearch(hosts=[ELASTIC_HOST])
    index_name = mappings_index
    recalls = json.loads(data)
    if not es.indices.exists(index_name):
        es.indices.create(
            index_name,
            body = mappings()
        )

    if delete_index:
        es.indices.delete(index=index_name, ignore=[400, 404])
    print('found '+ str(len(recalls)) + ' recalls')
    for recall in recalls :
        fulltext =setfulltext(recall)
        recallNumber = recall['RecallNumber']
        print('indexing recall number ' + recallNumber)
        es.index(
           index=index_name,
           id=recallNumber,
           doc_type="recall",
           body= fulltext
           )
    #update_job_history(job_name="recalls_to_elasticsearch")
    
def setfulltext(recall):
    #loop over recall keys - if key is list of dict- perform list comp to concat all string values
    seperator = ' '
    l = []
    #for key in recall.keys():
     #   print(type(recall[key]))
     #   if type(recall[key]) is type([]):
     #       print("Yes " + recall[key] + " a list")
    #time.sleep(10)
    #exit()
    l.append(seperator.join([seperator.join(r.values()) for r in recall['Products']]))
    l.append(seperator.join([seperator.join(r.values()) for r in recall['Injuries']]))
    l.append(seperator.join([seperator.join(r.values()) for r in recall['Manufacturers']]))
    l.append(seperator.join([seperator.join(r.values()) for r in recall['Importers']]))
    l.append(seperator.join([seperator.join(r.values()) for r in recall['Distributors']]))
    l.append(seperator.join([seperator.join(r.values()) for r in recall['Retailers']]))
    l.append(seperator.join([seperator.join(r.values()) for r in recall['Hazards']]))
    l.append(seperator.join([seperator.join(r.values()) for r in recall['Remedies']]))
    l.append(seperator.join([seperator.join(r.values()) for r in recall['ProductUPCs']]))
    l.append( seperator.join([seperator.join(r.values()) for r in recall['RemedyOptions']]))
    l.append(seperator.join([seperator.join(r.values()) for r in recall['Images']]))
    l.append(seperator.join([seperator.join(r.values()) for r in recall['Inconjunctions']]))
    
    l.append(seperator.join([recall['RecallNumber'],recall['Title'],recall['Description'],recall['ConsumerContact']]))
    
    fulltext = seperator.join(l)
    
    return {
        'TitleSuggest':{
            'input': tokenize(recall['Title'])
           
        },
        'Title':recall['Title'],
        'RecallNumber':recall['RecallNumber'],
        'Fulltext':fulltext,
        'ConsumerContact': recall['ConsumerContact'],
        'Products':recall['Products'],
        'Injuries': recall['Injuries'],
        'Manufacturers':recall['Manufacturers'],
        'ManufacturerCountries':recall['ManufacturerCountries'],
        'Importers': recall['Importers'],
        'Distributors': recall['Distributors'],
        'Retailers': recall['Retailers'],
        'Hazards': recall['Hazards'],
        'Remedies': recall['Remedies'],
        'RemedyOptions': recall['RemedyOptions'],
        'Images': recall['Images'],
        'Inconjunctions' : recall['Inconjunctions'],
        'ProductUPCs': recall['ProductUPCs'],
        'RecallDate': recall['RecallDate']
        }
             
def tokenize(input) :
    tokenized = []
    tokenized.append(input)
    tokens = input.split(' ')
    tokenized.extend(tokens)
    return tokenized


ELASTIC_HOST = os.getenv("ELASTIC_HOST")
if ELASTIC_HOST is None:
    print(' ELASTIC_HOST conn string is none')
ELASTIC_PORT = os.getenv("ELASTIC_PORT")
INDEX_PATTERN = "recalls"
#ELASTIC_SEARCH_URL = 'http://' + ELASTIC_HOST + ':' + str(ELASTIC_PORT)
INDEX_PREFIX = "cpsc-"
mongo_conn_str = os.getenv('PROD_MONGODB')
print(mongo_conn_str)
if mongo_conn_str is None:
    print('PROD_MONGODB conn string is none')
    exit()
mClient = MongoClient(mongo_conn_str)
db = mClient.neiss_test

SERVICE_ROOT = "https://www.saferproducts.gov/RestWebServices/Recall" 

last_run_date =get_recall_run_date()
today = last_run_date.strftime("%Y-%m-%d")
print(today)
if datetime.datetime.today() > last_run_date:
   data = get_recalls_api_data(SERVICE_ROOT,today)
   #load_recalls_data(data.json)
   #data,es, index_name, delete_index=False
   index_recalls(data.text,INDEX_PREFIX + INDEX_PATTERN,False)
  
  



    

