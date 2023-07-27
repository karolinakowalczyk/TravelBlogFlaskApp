from flask import Flask, redirect, request
from views import site
import os

app = Flask(__name__)

app.secret_key = 'secret'

app.register_blueprint(site, url_prefix="")

@app.before_request
def redirect_to_www_and_https():
    # Redirect non-www requests to www version (Heroku only)
    if 'DYNO' in os.environ and not request.url.startswith('https://www.'):
        return redirect(request.url.replace('https://', 'https://www.'), code=301)

if __name__ == "__main__":
    app.run()
