from flask import Blueprint , jsonify , request 
from mongo import get_db
from bson import ObjectId

user_delete = Blueprint('delete_user' , __name__)


@user_delete.route("/user/<id>" , methods = ["DELETE"])
def delete_user(id): 
    client = get_db()['db']['user']
    id = ObjectId(id)

    try : 
        client.delete_one({"_id" : id})
        return f"User of id {str(id)} Deleted Successfully"
    except Exception as e: 
        user = client.find_one({"_id" : id})
        print(e)
    return f"No user found of id {str(id)}"

