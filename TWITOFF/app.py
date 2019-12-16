"""Main application for Twitoff"""

#imports
from flask import Flask

#create app factory
#creates and configure an instance of a flask app
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def root():
        print("Welcome to our app")
    return app 
