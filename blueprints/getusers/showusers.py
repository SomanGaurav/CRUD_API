from flask import Blueprint , jsonify
from mongo import get_db 

from bson import ObjectId

users = Blueprint('get_users' , __name__)

from blueprints.getusers.checkusers import checkuser    
@users.route("/user" , methods = ["GET"])
def get_users(): 
     
    client = get_db()['db']['user']
    users = client.find()

    user_list = checkuser(users) 
    
    if not user_list : 
        return f"No user Found"

    return jsonify(user_list)



@users.route("/user/<id>" , methods=["GET"])
def get_specific_user(id): 
    
    client = get_db()['db']['user']
    oid = ObjectId(id)
    user = client.find_one({"_id" : oid})
    user_list = checkuser([user])
    
    if not user_list : 
        return f"No user found with id {id}"
    
    # user["_id"] = str(user["_id"])

    return user
