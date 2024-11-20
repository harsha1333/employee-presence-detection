import requests
import time
import json
import datetime
from dateutil import parser
url="https://api.thingspeak.com/channels/2602889/feeds/last.json?api_key-957P5WEGBHC5S3R3"

def readinfo():
    response=requests.get(url)
    ts=datetime.datetime.now
    #print(response.text)
    #print(ts)
    data=json.loads(response.text)
    #print(data)
    #print("Id: ",data['field1'])
    return data
        
def convert(utc_time):
    try:
        # Parse string to datetime object using dateutil.parser
        utc_time = parser.isoparse(utc_time)
        # IST is 5 hours and 30 minutes ahead of UTC
        ist_time = utc_time + datetime.timedelta(hours=5, minutes=30)
        # Convert datetime object back to string
        return ist_time.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        return str(e)

