from flask import Flask, request, redirect, url_for 
from flask_sqlalchemy import SQLAlchemy 
import os 

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URI")

db = SQLAlchemy(app)

class Owner(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), default="John")
    last_name = db.Column(db.String(30), unique=True)
    cars = db.relationship("Car", backref="ownerbr")

class Car(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_plate = db.Column(db.String(30), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey("owner.id"), nullable=False)

@app.route("/")
def home():
    return "<h1>This is a title</h1>"

@app.route("/postoption", methods=["GET", "POST"])
def posto():
    response = request.method
    return f"Method is {response}"

# Every single app will have the following 2 lines of code exactly
if __name__ == "__main__": 
    app.run(debug=True, host ="0.0.0.0", port=5000) 
# Port 5000 can only be for one service so will need to change this when I have more than one app 

# All of the lines above are all that flask requires to run an app

# app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:@localhost:3306/MyDatabase"
# Replace mydatabase with whatever you named your database
# = "sqlite:///data.db"
# to hide password do: os.getenv("DATABASE_URI") then type in terminal 
# export DATABASE_URI='mysql+pymysql://root:@localhost:3306/MyDatabase'