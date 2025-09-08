from flask import Flask,render_template,request
from datetime import datetime
import requests

BACKEND_URL = "http://127.0.0.1:9000"

app = Flask(__name__)

@app.route('/')
def home():

    day_of_week = datetime.now().strftime("%A")

    current_time = datetime.now().strftime("%H:%M:%S")

    return render_template('index.html', day=day_of_week, time=current_time)

@app.route('/submit',methods=['POST'])
def submit():
    form_data = request.form.to_dict()
    requests.post(f"{BACKEND_URL}/submit", json=form_data)

    return 'data submitted successfully to backend'

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000,debug=True)