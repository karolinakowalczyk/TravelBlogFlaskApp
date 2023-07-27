from flask import Flask, redirect, request
from views import site
import os

app = Flask(__name__)

app.secret_key = 'secret'

app.register_blueprint(site, url_prefix="")

if __name__ == "__main__":
    app.run()
