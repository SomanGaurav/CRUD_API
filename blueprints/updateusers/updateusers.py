from flask import Blueprint , jsonify , request 
from mongo import get_db
from bson import ObjectId

user_update = Blueprint('update_user' , __name__)


@user_update.route("/user/<id>" , methods = ["PUT"])
def update_user(id): 
     
    client = get_db()['db']['user']
    id = ObjectId(id)
    user = client.find_one({"_id" : id})

    if not user : 
        return f"User with id {str(id)} not found" 
    

    user["_id"] = str(user["_id"])
    for i in request.form : 
        user[i] = request.form.getlist(i)[0]
    del user['_id'] 
    try : 
        client.update_one({"_id" : id } , {'$set' : user})

    except Exception as e : 
        return f"Failed to update user try after some time"

    return user 