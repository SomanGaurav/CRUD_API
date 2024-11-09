from pymongo.mongo_client import MongoClient
import os


def get_db():   
    username = os.environ.get("MONGODB_USERNAME")
    password = os.environ.get("MONGODB_PASSWORD")
    client = MongoClient(host='mongo' , port=27017 ,username=username, password=password ,authsource = 'admin')

    try : 
        client.admin.command('ping')
        print("Pinged to local DB") 
    except Exception as e : 
        print(e)

    return client 
