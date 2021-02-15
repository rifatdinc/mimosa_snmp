#!/usr/bin/python3
from flask import Flask, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
import snmp
import json
import time
app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:mypasswords@localhost/postgres'
db = SQLAlchemy(app)


# @app.route('/')
# def sql():

#     sqlName = snmp.sql()
#     return json.dumps(sqlName)


@app.route('/')
def runnning():
    snmP = snmp.saymaMakinesi()
    return json.dumps(snmP)


# app.run(host='0.0.0.0')

