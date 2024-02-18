from flask import Flask, jsonify
from flask_cors import CORS
from src import main

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    return jsonify({'message': 'Cyclic Tasks is running...'})


if __name__ == '__main__':
    app.run()