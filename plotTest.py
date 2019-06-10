#realtimefirebase_2 ver.
#
#
import pyrebase
from flask import Flask
from flask import request
from timestamp import *
from firebase_admin import credentials
from firebase_admin import db as db2
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


getData()
