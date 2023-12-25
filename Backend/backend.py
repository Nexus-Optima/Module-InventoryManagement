from flask import Flask, jsonify, request
from flask_cors import CORS
from Execute.execute import execute
from Utils.send_email import send_email
import logging
from dotenv import load_dotenv

app = Flask(__name__)
cors = CORS(app)
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


@app.route('/', methods=['GET'])
def inventory_management():
    try:
        result = execute()
        return jsonify(result.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


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
