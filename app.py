from flask import Flask, redirect, request
from views import site
from flask_talisman import Talisman
from flask_compress import Compress
from urllib.parse import urlparse, urlunparse

app = Flask(__name__, static_folder='static', static_url_path='')

app.secret_key = 'secret'

app.register_blueprint(site, url_prefix="")

Talisman(app, content_security_policy=None)

Compress(app)

@app.before_request
def redirect_nonwww():
    """Redirect non-www requests to www."""
    urlparts = urlparse(request.url)
    if urlparts.netloc == 'travel-blog-flask-app-5d928a87ede1.herokuapp.com':
        urlparts_list = list(urlparts)
        urlparts_list[1] = 'www.travel-blog-flask-app-5d928a87ede1.herokuapp.com'
        return redirect(urlunparse(urlparts_list), code=301)

if __name__ == "__main__":
    app.run(debug=False)
