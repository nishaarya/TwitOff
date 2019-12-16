#import flask package
#flask makes app objects
from flask import Flask

#creat Flask web server
#This makes the application
app = Flask(__name__)

#routes determine the location
@app.route('/')

#define a simple function
def hello():
    print('Hello World!')
