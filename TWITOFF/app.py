"""Main application for Twitoff"""

#imports
from decouple import config
from flask import Flask, render_template, request
from .models import DB, User

#create app factory
#creates and configure an instance of a flask app
def create_app():
    app = Flask(__name__)

    #add config for database
    app.config['SQLALCHEMY_DATABASE_URI'] = config('DATABASE_URL')

    #stop tracking modifications on sqlalchemy config
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    #have the database know about the app
    DB.init_app(app)

    @app.route('/')
    def root():
        users = User.query.all()
        return render_template('base.html', title = 'Home', users=users)
    return app
