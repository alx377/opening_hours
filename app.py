from flask import Flask, request
from utils import parse_data
app = Flask(__name__)

@app.route('/', methods=['POST'])
def opening_hours():
    if request.method == 'POST':
        data = parse_data(request.json)
        return data
