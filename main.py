from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route('/hello')
def index():
    return jsonify({"Choo Choo": "Token"})


if __name__ == '__main__':
    app.run(debug=True, port=os.getenv("PORT", default=5000))
