from flask import Flask, request
from dotenv import load_dotenv
import os
import pymongo
load_dotenv()  # take environment variables from .env.
MONGO_URI = os.getenv("MONGO_URI")


from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Create a new client and connect to the server
client = MongoClient(MONGO_URI, server_api=ServerApi('1'))
db=client.test
collection = db['flask_test']


app = Flask(__name__)


@app.route('/submit', methods=['POST'])
def submit():
    form_data = request.json   # already a dict
    collection.insert_one(form_data)
    return "Form submitted successfully!"

@app.route('/view')

@app.route('/view')
def view():
    records = list(collection.find())
    for item in records:
        del item['_id'] 
    return {"records": records}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000, debug=True)