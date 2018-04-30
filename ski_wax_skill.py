from flask import Flask
from flask_ask import Ask, statement, question, session
import json
import requests
import time
import unidecode

app = Flask(__name__)
ask = Ask(app, "/ski_wax")

def get_weather():
    pass

@app.route('/')
def homepage():
    return "What wax will you need to use?"

@ask.launch
def start_skill():
        welcome_message = 'Hello there, would you like to know what wax you should use'

@ask.intent("YesIntent")
def low_wax():
    low_temp = 'What will the low temperature in degrees celcius be between 8 AM and 4 PM?'
    return question(low_temp)

def high_wax():
    high_temp = 'What will the high temperature in degrees celcius be between 8 AM and 4 PM?'
    return question(high_temp)

lf_wax ={
    'LF10':5.0 #0 to 10
    'LF8':0 #-4 to 4
    'LF7':-5.0 #-2 to -8
    'LF6':-7.5 #-5 to -10
    'LF5':-11 #-8 to -14
    'LF4':-14 #-12 to -32
    }


@ask.intent("NoIntent")
def bye_text():
    bye_text = 'Okay bye I guess, good luck at your race or training day tomorrow'
    return statement(bye)

if __name__ == '__main__':
    app.run(debug=True)
