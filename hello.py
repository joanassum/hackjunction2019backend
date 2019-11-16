from flask import Flask
from flask import request
import alerts1
import page_checker

app = Flask(__name__)

@app.route('/check-phishing')
def hello_world():
    url = request.args.get('url')
    return page_checker.get_issues(url)
