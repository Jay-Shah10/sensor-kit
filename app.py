from flask import Flask
import RPi.GPIO as GPIO
import logging

app = Flask(__name__)



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)



