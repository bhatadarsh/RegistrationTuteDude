from flask import Flask, render_template, request, redirect, url_for, flash
from pymongo import MongoClient
from dotenv import load_dotenv
import os
load_dotenv() 

app = Flask(__name__)
app.secret_key = "supersecret" 


MONGO_URI = os.getenv("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["test_db"]
collection = db["flask_form"]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']

        
        collection.insert_one({"name": name, "email": email})

        return redirect(url_for('success'))
    except Exception as e:
        
        flash(str(e))
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return "Data submitted successfully!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)
