from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return 'Hi Jaimie, Richie, and Bobby!  How are you today?'
