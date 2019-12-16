"""SQLAlchemy models for Twitoff"""

#import
from flask_sqlalchemy import SQLAlchemy

#create a database
DB = SQLAlchemy()

#Twitter users that we pull and analyse
class User(DB.Model):
    id  = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)

#Tweets
class Tweet(DB.Model):
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.Unicode(280))
