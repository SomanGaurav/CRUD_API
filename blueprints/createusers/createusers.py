from flask import Blueprint , jsonify , request 
from mongo import get_db

creator = Blueprint('create_user' , __name__)


@creator.route("/user" , methods = ["POST"])
def create_user(): 
    client = get_db()['db']['user']
    username = request.form.get('username')
    email = request.form.get('email') 
    password = request.form.get('password') 
    user_dict = {'username' : username , 'email' : email , 'password' : password} 
    try : 
        client.insert_one(user_dict)
    except : 
        print("error")
    return f"User data {username} and {email} and {password}"

