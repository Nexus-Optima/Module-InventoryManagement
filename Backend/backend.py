from flask import Flask, jsonify
from Execute.execute import execute
app = Flask(__name__)


@app.route('/inventory_management', methods=['GET'])
def inventory_management():
    try:
        result = execute()
        return jsonify(result.to_dict(orient='records'))
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)