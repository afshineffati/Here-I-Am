from flask import Flask

app = Flask(__name__)  #it is tipycal to have the variable called app

from my_app import routes