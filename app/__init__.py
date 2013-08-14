from flask import Flask

app = Flask(__name__)
# no config for now
#app.config.from_object('config')

from app import views
