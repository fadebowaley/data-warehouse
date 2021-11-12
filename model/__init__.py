from app import app
from flask import request, session,flash
from helpers.database import *
from helpers.hashpass import *
from helpers.mailer import *
from bson import json_util, ObjectId
import datetime
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
    sendmail(subject="Registration for Flask Admin Boilerplate", sender="Flask Admin Boilerplate", recipient=user_data["email"], body="You successfully registered on Flask Admin Boilerplate")
    print("Done")
    
def add_section():
      section=request.form.get("section")
      market=request.form.get("market")
      section_items.insert_one({"Section_name":str(section),"Market":str(market),"Date_created":datetime.datetime.now(),"Section":True})
      flash('you successfully create a section')


def add_new_items():
    fields = [k for k in request.form]                                      
    values = [request.form[k] for k in request.form]
    data = dict(zip(fields, values))
    item_data = json.loads(json_util.dumps(data))
    print(item_data)    
    # x = item_data['item1']
    # y = item_data['item2']
    # a = item_data['item3']
    # z = item_data['item4']
    # print(x,y,a,z)    
    # items.insert(items_data)



      

    #items.insert_one({"items1":item1,"item2":str(item2),"item3":str(item3),"item4":str(item4),"item5":str(item5)"})
                      
        