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
port_list = {}

app = Flask(__name__)



@app.route("/")
def index():
    return "Hello World!"

@app.route('/create/<servername>')
def create(servername):
    global serverlist
    global port_list
    if servername in serverlist:
        return "Server name %s is already exist." % servername
    serverlist.append(servername)
    port_number = 0
    if request.remote_addr in port_list:
        port_list[request.remote_addr] += 50
        port_number = port_list[request.remote_addr]
    else:
        port_number = 8000 + (int(request.remote_addr.split(".")[3])%10)*10
        port_list[request.remote_addr] = port_number
    os.system("touch %s" % servername)
    os.system("mkdir /home/ensyuu2/docker/%s" % servername)
    html = """<html><body><font size = "16">%s is running!</font></body></html>""" % servername
    os.system('echo  "%s" > /home/ensyuu2/docker/%s/index.html' %(html, servername))
    docker_cmd = ' docker run --name %s -p %d:80 -v "/home/ensyuu2/docker/%s/:/var/www/html/" -d php:5.6-apache' % (servername, port_number, servername)
    os.system(docker_cmd)
    return "Port number:%d"%port_number
@app.route('/delete/<servername>')
def delete(servername):
    if servername not in serverlist:
        return "Server name %s is not exist." % servername
    else:
        serverlist.remove(servername)
    os.system("rm -r /home/ensyuu2/docker/%s"%servername)
    os.system("docker stop $(docker ps -a |grep %s | awk '{print $1;}')" % servername )
    os.system("docker rm $(docker ps -a |grep %s | awk '{print $1;}')" % servername )
    return "delete %s." % servername

@app.route('/show')
def show():
    #url = 'curl -X POST -H "Content-Type:application/json" -d "%s" http://%s/test.php' % (escape(json.dumps({"servername":serverlist})),request.remote_addr)
    url = 'curl -X POST -H "Content-Type:application/json" -d "%s" http://192.168.1.102/test.php' % (escape(json.dumps({"servername":serverlist})))
    print url
    print request.remote_addr
    os.system(url)

    return json.dumps({"servername":serverlist})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80,debug=True)
