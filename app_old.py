import pyrebase
from flask import Flask
from flask import request
from timestamp import *
from firebase_admin import credentials
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

## push individual bottles
#curTime = timestamp()
#rfid = str(random.randint(101,106))+'-'+str(random.randint(1,200))
#bottletype = random.randint(0,12)
#db.push({"RFID":rfid, "time": curTime , "type" : bottletype})
#
#
#users = db.get()
#print(users.key())

from flask import *

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
        result_string ="There are << "+str(len(to))+" >> TYPE "+str(input_text)+" in database"
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
                search_by_RFID()
            
            
       
#            if(request.form.get('searchfield',None)!=None):
#               input_text = int(request.form.get('searchfield',None))
#               if(input_text>12):
#                   result_string = "Error : Type must be in range(0,12)"
#                   return render_template('index.html', f1=result_string,t = to.values())
#               print("input text is => "+str(input_text))
#               result = db.order_by_child('type').equal_to(input_text).get()
#               to = result.val()
#               result_string ="There are << "+str(len(to))+" >> TYPE "+str(input_text)+" in database"
#               print("request variable modified")
#
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
