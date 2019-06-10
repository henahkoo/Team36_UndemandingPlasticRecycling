#realtimefirebase_2 ver.
#
#
import pyrebase
from flask import Flask, request, redirect, url_for, send_from_directory, render_template
from flask import request
from timestamp import *
from firebase_admin import credentials
from firebase_admin import db as db2
from werkzeug import secure_filename
import os
import json


config = {
    "apiKey" : "AIzaSyBNFcWJUioeQBl1sd-x4w3RSMHqTsSpCP0",
    "authDomain" : "upr-team36.firebaseapp.com",
    "databaseURL" : "https://upr-team36.firebaseio.com",
    "projectId" : "upr-team36",
    "storageBucket" : "upr-team36.appspot.com",
    "messagingSenderId" : "971091089423"
}

firebase = pyrebase.initialize_app(config)

db = firebase.database()

def pushdata(type):
# push individual bottles
    curTime = timestamp()
    rfid = str(random.randint(101,106))+'-'+str(random.randint(1,200))
    bottletype = type
    machine = random.randint(1,3)
    db.push({"machine":machine, "RFID":rfid, "time": curTime.replace('"','') , "type" : bottletype})

def getData():
    m1= open("machine1.txt","w+")
    m2= open("machine2.txt","w+")
    m3= open("machine3.txt","w+")
    timeResult = db.order_by_child('time').get()
    for trash in timeResult.each():
        if(trash.val()['machine']==1):
            m1.write(trash.val()['time'][:2]+"\n")
            print("machine 1 => ",end='')
            print(trash.val()['time'])
        if(trash.val()['machine']==2):
            m2.write(trash.val()['time'][:2]+"\n")
            print("machine 2 => ",end='')
            print(trash.val()['time'])
        if(trash.val()['machine']==3):
            m3.write(trash.val()['time'][:2]+"\n")
            print("machine 3 => ",end='')
            print(trash.val()['time'])

users = db.order_by_child('time').get()
app = Flask(__name__)

def search_by_type():
    print("\n\n <<<<<<<<<<Search by type selected>>>>>>>>>>>\n\n")
    if(request.form.get('searchfield',None)!=None):
        input_text = int(request.form.get('searchfield',None))
        if(input_text>12):
            result_string = "Error : Type must be in range(0,12)"
            return render_template('index.html', f1=result_string,t = to.values())
        print("input text is => "+str(input_text))
        result = db.order_by_child('type').equal_to(input_text).get()
        to = result.val()
        result_string ="There are < "+str(len(to))+" > bottles with TYPE < "+str(input_text)+" > in database"
        print("request variable modified")
        return result_string,result

def search_by_RFID():
    print("\n\n <<<<<<<<<<Search by RFID selected>>>>>>>>>>>\n\n")
    if(request.form.get('searchfield',None)!=None):
        input_text = int(request.form.get('searchfield',None))
        if((101>input_text)or(input_text>106)):
            result_string = "Error : RFID must be in range(101,106)"
            return render_template('index.html', f1=result_string,t = to.values())
        result = db.order_by_child('RFID').start_at(str(input_text)).end_at(str(input_text+1)).get()
        to = result.val()
        result_string ="There are < "+str(len(to))+" > bottles with RFID < "+str(input_text)+" > in database"
        print("request variable modified")
        return result_string,result

def search_by_machine():
    print("\n\n <<<<<<<<<<Search by Machine selected>>>>>>>>>>>\n\n")
    if(request.form.get('searchfield',None)!=None):
        input_text = int(request.form.get('searchfield',None))
#        if((101>input_text)or(input_text>106)):
#            result_string = "Error : RFID must be in range(101,106)"
#            return render_template('index.html', f1=result_string,t = to.values())
        result = db.order_by_child('machine').equal_to(input_text).get()
        to = result.val()
        result_string ="There are < "+str(len(to))+" > bottles in MACHINE < "+str(input_text)+" > in database"
        print("request variable modified")
        return result_string,result

@app.route('/', methods=['GET', 'POST'])
def basic():
    if request.method == 'POST':
        if request.form['submit'] == 'search':
            input_text = 0
            type = request.form.getlist('type')
            result = db.get()
            to = result.val()

            selmenu = request.form.get("droplist")
            if(selmenu == "type"):
                result_string,result = search_by_type()
                to = result.val()
            if(selmenu == "RFID"):
                result_string, result = search_by_RFID()
                to = result.val()
            if(selmenu == "machine"):
                result_string,result = search_by_machine()
                to = result.val()

            for trash in result.each():
                print(trash.key())
                print(trash.val())
                print("next trash")
            print(result_string)
            return render_template('index.html', f1=result_string,t = to.values())


        return render_template('index.html')
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
