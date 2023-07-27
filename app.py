from flask import Flask, redirect, request
from views import site
from flask_talisman import Talisman
from flask_compress import Compress

app = Flask(__name__, static_folder='static', static_url_path='')

app.secret_key = 'secret'

app.register_blueprint(site, url_prefix="")

Talisman(app, content_security_policy=None)

Compress(app)

@app.before_request
def redirect_non_www():
    if request.headers.get('Host') == 'www.travel-blog-flask-app-9b69d584e4f3.herokuapp.com':
        new_url = request.url.replace('www.', '', 1)
        return redirect(new_url, code=301)

if __name__ == "__main__":
    app.run(debug=False)
