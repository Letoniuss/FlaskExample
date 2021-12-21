from flask import Flask
application = Flask(__name__)

@application.route('/')
def hello_world():
    return "Oh, so you were looking to run a report? Well, I can't do that but I can ask how you are doing today! How are you?"

