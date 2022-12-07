# this is the "web_app/routes/home_routes.py" file...
# test

from flask import Blueprint, request, render_template

home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
@home_routes.route("/home")
def index():
    return render_template("home.html")

@home_routes.route("/convert")
def convert():
    return render_template("convert.html")



