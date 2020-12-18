#REST API with Flask for Endocode technical challenge Level 1
#Kevin Donnelly

#Imports
from flask import Flask, request, json
import logging
import subprocess
import re
import os
import sys

#Log (Listening port, date, HTTP status, request) to log file
logging.basicConfig(filename='Structured.log', level=logging.DEBUG)

#Create an instance of Flask
app = Flask(__name__)

# /helloworld returns 'Hello Stranger' 
# http://0.0.0.0:8080/helloworld

#/helloworld?name=AlfredENeumann (any filtered value) returns 'Hello Alfred E Neumann'
# http://0.0.0.0:8080/helloworld?name=
@app.route('/helloworld', methods=['GET'])
def hello_world():
    if request.args:
        query_name = request.args.get("name", "")
        user_name = (re.sub(r"(?<=\w)([A-Z])", r" \1", query_name)).title()
        return f"Hello {user_name}"
    else:
        return f'Hello Stranger'

# Returns a JSON with Githash and name of the project
# http://0.0.0.0:8080/versionz
@app.route('/versionz')
def get_git_revision_hash():
    latest_commit_hash = subprocess.check_output(['git', 'rev-parse', 'HEAD'])
    project_name = os.path.basename(os.path.abspath(__file__))
    values = {f"{project_name}": f"{latest_commit_hash}"}
    return json.dumps(values)
