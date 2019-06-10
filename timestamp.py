from datetime import datetime
import random
from firebase_admin import credentials
import json

def timestamp():
    start_date = datetime.now().strftime('%d%b%Y %H:%M:%S')
    d = start_date
    return json.dumps(d)
