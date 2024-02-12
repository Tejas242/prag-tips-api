from flask import Flask, jsonify
import json
import random

app = Flask(__name__)

# Function to load tips data from JSON file
def load_tips_data():
    with open('./prag-tips.json', 'r') as file:
        tips_data = json.load(file)
    return tips_data

# API endpoint to fetch a random tip
@app.route('/tips/random', methods=['GET'])
def get_random_tip():
    tips_data = load_tips_data()
    print(tips_data)
    random_tip = random.choice(tips_data)
    return jsonify(random_tip)

if __name__ == '__main__':
    app.run(debug=True)
