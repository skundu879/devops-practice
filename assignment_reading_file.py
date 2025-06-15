# app.py
import os
import json
from flask_pymongo import PyMongo
from flask import Flask, jsonify
from configParser import parse_config_file

CONFIG_FILE = 'config.txt'

app = Flask(__name__)
app.config['MONGO_URI'] = 'mongodb+srv://user:test123db@devops-db.ia3nuoj.mongodb.net/devopsDb?retryWrites=true&w=majority&appName=devops-db'
mongo = PyMongo(app)
db = mongo.db

def read_config(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Config file '{file_path}' not found.")
    config_dict = parse_config_file(file_path)
    print(config_dict)
    return config_dict

def save_to_db(data):
    db.config_data.insert_one(data)



def fetch_from_db():
    data = db.config_data.find_one({})
    if data:
        return data
    return {}

@app.route('/config', methods=['GET'])
def get_config():
    try:
        data = fetch_from_db()
        return jsonify(data), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    try:
        config_data = read_config(CONFIG_FILE)
        save_to_db(config_data)
        print("Configuration loaded and saved to database.")
    except Exception as e:
        print(f"Error: {e}")
    app.run(debug=True)
