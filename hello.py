from flask import Flask
from flask import request
import alerts1
import page_checker

app = Flask(__name__)

@app.route('/check-phishing')
def hello_world():
    url = request.args.get('url')
    data1 = alerts1.computeAlerts(url)
    if data1 != []:
        data = {}
        data['isPhishing'] = True
        try: 
            data2 = page_checker.get_issues(url)
            data['issues'] = data2['issues'] + data1
            return data
        except:
            data['issues'] = data1
            return data

    else: 
        data = {}
        data['isPhishing'] = False
        return data
