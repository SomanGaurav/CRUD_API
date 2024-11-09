from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os

uri = "mongodb+srv://gaurav:gaurav@cluster0.k5pd2.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"


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



 # try : 
    #     client = MongoClient(host='mongo' , port='27017' ,username='gaurav' , password='gaurav')
    #     try : 
    #         client.admin.command('ping')
    #         print("Pinged your local DB . You successfully connected to MongoDB!")

    #     except : 
    #         print("Failed to connect to local DB")

    # except : 
    #     client = MongoClient(uri, server_api=ServerApi('1'))
    #     try:
    #         client.admin.command('ping')
    #         print("Pinged your deployment. You successfully connected to MongoDB!")
    #     except Exception as e:
    #         print(e)