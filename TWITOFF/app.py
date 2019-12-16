"""Main application for Twitoff"""

#imports
from flask import Flask
from .models import DB

#create app factory
#creates and configure an instance of a flask app
def create_app():
    app = Flask(__name__)

    #add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
    DB.init_app(app)

    @app.route('/')
    def root():
        return "Welcome to our app"
    return app
