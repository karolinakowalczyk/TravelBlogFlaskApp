from flask import Flask
from views import site
#from flask_talisman import Talisman
from flask_compress import Compress

app = Flask(__name__, static_folder='static', static_url_path='')

app.secret_key = 'secret'

app.register_blueprint(site, url_prefix="")

#Talisman(app, content_security_policy=None)

Compress(app)

if __name__ == "__main__":
    app.run(debug=False)
