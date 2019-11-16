from flask import Flask
from flask import request
import alerts1

app = Flask(__name__)

@app.route('/check-phishing')
def hello_world():
    url = request.args.get('url')
    data = {}
    data['isPhishing'] = is_phishing(url)
    return data

def is_phishing(url):
    print(url)
    print(alerts1.computeAlerts(url))
    return alerts1.computeAlerts(url) != []