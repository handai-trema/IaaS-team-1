# app.py
from flask import Flask, jsonify
import json
from flask import request
import os
import re

def escape(s, quoted=u'\'"\\', escape=u'\\'):
    return re.sub(
            u'[%s]' % re.escape(quoted),
            lambda mo: escape + mo.group(),
            s)


app = Flask(__name__)
serverlist = []



@app.route("/")
def index():
    return "Hello World!"

@app.route('/create/<servername>')
def create(servername):
    serverlist.append(servername)
    #os.system("touch %s" % servername)
    return 'Thanks post: id = %s' % servername

@app.route('/show')
def show():

    url = 'curl -X POST -H "Content-Type:application/json" -d "%s" http://%s/test.php' % (escape(json.dumps({"servername":serverlist})),request.remote_addr)
    print url
    print request.remote_addr
    os.system(url)

    return ""


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
