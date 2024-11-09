from flask import Flask 
import os


from blueprints.getusers.showusers import users
from blueprints.createusers.createusers import creator
from blueprints.updateusers.updateusers import user_update
from blueprints.deleteusers.deleteusers import user_delete



app = Flask(__name__)


app.register_blueprint(users)
app.register_blueprint(creator)
app.register_blueprint(user_update)
app.register_blueprint(user_delete)


@app.route("/")
def home(): 
    return "Hello World" 


if __name__ == '__main__': 
    app.run(debug = True , host="0.0.0.0",port = os.environ.get("APP_PORT"))