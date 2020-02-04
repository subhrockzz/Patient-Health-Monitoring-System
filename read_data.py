#!/usr/bin/env python3

import sys
import os
import serial
import flask
from flask import request, jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True

condition = [
    {'Patient Name': 'SUBHRAJEET ROY',
     'Temperature': 98,
     'Pulse Rate': 72,
     'Systole': 60,
     'Diastole': 70},
    {'Patient Name': 'SUBHRAJEET ROY',
     'Temperature': 98,
     'Pulse Rate': 72,
     'Systole': 60,
     'Diastole': 70},
    {'Patient Name': 'SUBHRAJEET ROY',
     'Temperature': 98,
     'Pulse Rate': 72,
     'Systole': 60,
     'Diastole': 70},
]

#ser = serial.Serial('/dev/ttyArduino', 115200, 8,'N', 1, timeout=5)

#name = raw_input("Enter your name : ")
#email = raw_input("Enter your email : ")
#no = raw_input("Enter your contact no : ")
#age =int( raw_input("Enter your age : "))
#gender = raw_input("Enter your gender : ")
@app.route('/', methods=['GET'])
def home():
    return json.dumps(condition)

app.run()


#while True:
   # data = ser.readline()
    #print ("--->",data)
    #print("\n")
    #time.sleep(1)

#print ("Done")
