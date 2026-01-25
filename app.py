from http import client
from flask import Flask, request, render_template, url_for, jsonify
from dotenv import load_dotenv
import os
import pymongo
import json

load_dotenv()

Mongo_URL = os.getenv("URL")

client = pymongo.MongoClient(Mongo_URL)
db = client.test

collection = db['flask_test']

app = Flask(__name__)
@app.route('/')
def home():
    return render_template('index.html')
    
@app.route('/submittodoitem', methods=['POST'])
def submittodoitem():
   
    data = request.get_json()
    itemname = data.get('itemname')
    itemdescription = data.get('itemdescription')

    if not itemname or not itemdescription:
        return jsonify({'error': 'Item name and description are required.'}), 400
    

    todo_item = {
        'itemname': itemname,
        'itemdescription': itemdescription
    }

    collection.insert_one(todo_item)

    return jsonify({'message': 'To-Do item added successfully!'}), 201

if __name__ == '__main__':
    app.run(debug=True)