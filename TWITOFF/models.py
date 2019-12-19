"""SQLAlchemy models for Twitoff"""

#import
from flask_sqlalchemy import SQLAlchemy

#create a database
DB = SQLAlchemy()

#Twitter users that we pull and analyse
class User(DB.Model):
    """Twitter users that we analyze"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    name = DB.Column(DB.String(15), nullable=False)
    newest_tweet_id = DB.Column(DB.BigInteger)
    def __repr__(self):
        return '<User {}>'.format(self.name)

#Tweets
class Tweet(DB.Model):
    """Tweets we pull"""
    id = DB.Column(DB.BigInteger, primary_key=True)
    text = DB.Column(DB.Unicode(300))
    user_id = DB.Column(DB.BigInteger, DB.ForeignKey('user.id'), nullable=False)
    user = DB.relationship('User', backref=DB.backref('tweets', lazy=True))

#Add the embedding
    embedding = DB.Column(DB.PickleType, nullable=False)

    def __repr__(self):
        return '<Tweet {}>'.format(self.text)
