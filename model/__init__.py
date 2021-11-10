from app import app
from flask import request, session
from helpers.database import *
from helpers.hashpass import *
from helpers.mailer import *
from bson import json_util, ObjectId
import json


def checkloginusername():
    username = request.form["username"]
    check = users.find_one({"username": username})
    if check is None:
        return "No User"
    else:
        return "User exists"

def checkloginpassword():
    username = request.form["username"]
    check = users.find_one({"username": username})
    password = request.form["password"]
    hashpassword = getHashed(password)
    if hashpassword == check["password"]:
        sendmail(subject="Login on Flask Admin Boilerplate", sender="Flask Admin Boilerplate", recipient=check["email"], body="You successfully logged in on Flask Admin Boilerplate")
        session["username"] = username
        return "correct"
    else:
        return "wrong"
    

def checkusername():
    username = request.form["username"]
    check = users.find_one({"username": username})
    if check is None:
        return "Available"
    else:
        return "Username taken"

def registerUser():
    fields = [k for k in request.form]                                      
    values = [request.form[k] for k in request.form]
    data = dict(zip(fields, values))
    user_data = json.loads(json_util.dumps(data))
    user_data["password"] = getHashed(user_data["password"])
    user_data["confirmpassword"] = getHashed(user_data["confirmpassword"])
    users.insert(user_data)
    sendmail(subject="Registration on Mile12 Data-wareHouse", sender="Flask Admin Boilerplate", recipient=user_data["email"], body="You successfully registered on Flask Admin Boilerplate")
    print("Done")
    

def add_section():
      section1=request.form.get("section")
    #   market=request.form.get("market")
      if section_items.find_one({"Status":"created"}):
            section=section_items.find_one({"Status":"created"})
            s=section['Section']
            s.append(str(section1))
            section_items.update_one({"Status":"created"},{"$set":{"Section":s}})   
      else:
            section_items.insert_one({"Section":[str(section1)],"Status":"created"})
            
            

def add_items():
    fields = [k for k in request.form]                                      
    values = [request.form[k] for k in request.form]
    data = dict(zip(fields, values))
    item_data = json.loads(json_util.dumps(data))
    print(item_data)
    items.insert(item_data) 
    print("Done")
            
    
       
               