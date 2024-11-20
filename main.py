from flask import Flask, render_template
import datetime
from functions import readinfo,convert
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    person=readinfo()
    ts=person['created_at']
    ts=convert(ts)
    return render_template('index.html', ts=ts)

@app.route('/detail',methods=['GET'])
def find():
    person=readinfo()
    p=bool(int((person['field1'])))
    ts=person['created_at']
    ts=convert(ts)
    print("Person is" ,p)
    #print("Timestamp is ",ts)
    return render_template('find.html', p=p,ts=ts)

if __name__ == '__main__':
    app.run(debug=True)
