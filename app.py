from flask import Flask, jsonify, request
from flask_cors import CORS 
import json
import random

app = Flask(__name__)
CORS(app)

# Function to load tips data from JSON file
def load_tips_data():
    with open('./prag-tips.json', 'r') as file:
        tips_data = json.load(file)
    return tips_data

@app.route('/', methods=['GET'])
def home():
    return "Welcome to Pragmatic Geih API!"

# API endpoint to fetch a random tip
@app.route('/tips/random', methods=['GET'])
def get_random_tip():
    tips_data = load_tips_data()
    print(tips_data)
    random_tip = random.choice(tips_data)
    return jsonify(random_tip)


@app.route('/tips', methods=['GET'])
def get_all_tips():
    tips_data = load_tips_data()
    return jsonify(tips_data)

if __name__ == '__main__':
    app.run(debug=True)
