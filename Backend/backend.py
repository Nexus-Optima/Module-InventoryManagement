from flask import Flask, jsonify, request
from flask_cors import CORS
from Execute.execute import execute, fetch_data, post_data
from Utils.send_email import send_email
import logging
import pandas as pd
from dotenv import load_dotenv

app = Flask(__name__)
cors = CORS(app)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

@app.route('/', methods=['GET'])
def inventory_management():
    try:
        data = execute()  
        post_data(data) 
        return jsonify({"message": "Data stored in S3 successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500    

@app.route('/fetch_data', methods=['GET'])
def fetch_data_endpoint():
    try:
        fetched_data = fetch_data()
        return fetched_data.to_json(orient='records'), 200
    except Exception as e:
        return jsonify({"error": "Failed to fetch data: " + str(e)}), 500

@app.route('/send-email', methods=['POST'])
def handle_send_email():
    data = request.json
    try:
        send_email(data['name'], data['email'], data['message'])
        return jsonify({"message": "Email sent successfully"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


load_dotenv()

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
