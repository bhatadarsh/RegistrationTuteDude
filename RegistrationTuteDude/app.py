from flask import Flask, request, render_template, jsonify
from pymongo import MongoClient
import os

app = Flask(__name__)

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
client = MongoClient(MONGO_URI)
db = client.todo_db
todos = db.todos

@app.route("/api")
def api():
    
    return jsonify({"message": "Hello from Flask To-Do App", "status": "initial"})


@app.route("/todo", methods=["GET"])
def todo_page():
    return render_template("todo.html")


@app.route("/submittodoitem", methods=["POST"])
def submit_todo():
    itemName = request.form.get("itemName")
    itemDescription = request.form.get("itemDescription")
    itemId = request.form.get("itemId")
    itemUUID = request.form.get("itemUUID")
    itemHash = request.form.get("itemHash")

    doc = {
        "itemName": itemName,
        "itemDescription": itemDescription,
        "itemId": itemId,
        "itemUUID": itemUUID,
        "itemHash": itemHash
    }
    todos.insert_one(doc)
    return "Item submitted successfully!", 201

if __name__ == "__main__":
    app.run(debug=True)
