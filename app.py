from flask import Flask, render_template
from views import site
import os

app = Flask(__name__)

app.register_blueprint(site, url_prefix="")

if __name__ == "__main__":
    app.run()
