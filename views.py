from flask import Blueprint, render_template
site = Blueprint('site', __name__, static_folder="static", template_folder='templates')

@site.route('/')
@site.route("/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date='2023'
    )