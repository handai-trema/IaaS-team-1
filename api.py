#!/usr/bin/env python
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

serverlist = []
port_number = 8000

app = Flask(__name__)



@app.route("/")
def index():
    return "Hello World!"

@app.route('/create/<servername>')
def create(servername):
    global port_number
    global serverlist
    serverlist.append(servername)
    port_number += 10
    # os.system("touch %s" % servername)
    os.system("mkdir /home/ensyuu2/docker/%s" % servername)
    html = """<html><body>%s is running!</body></html>""" % servername
    os.system('echo  "%s" > /home/ensyuu2/docker/%s/index.html' %(html, servername))
    docker_cmd = ' docker run --name %s -p %d:80 -v "/home/ensyuu2/docker/%s/:/var/www/html/" -d php:5.6-apache' % (servername, port_number, servername)
    os.system(docker_cmd)
    return "%d"%port_number

@app.route('/show')
def show():

    url = 'curl -X POST -H "Content-Type:application/json" -d "%s" http://%s/test.php' % (escape(json.dumps({"servername":serverlist})),request.remote_addr)
    print url
    print request.remote_addr
    os.system(url)

    return ""


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
