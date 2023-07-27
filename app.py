from flask import Flask, redirect, request
from views import site
import os

app = Flask(__name__, static_folder='static', static_url_path='')

app.secret_key = 'secret'

app.register_blueprint(site, url_prefix="")

if __name__ == "__main__":
    app.run()
