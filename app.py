import requests
from flask import Flask, render_template

app = Flask(__name__)

API_URL = 'http://localhost:8000/api/v1'

@app.route('/')
def index():
    roles = requests.get(f'{API_URL}/roles/')
    roles = roles.json()

    return render_template('index.html', roles=roles)