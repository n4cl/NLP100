# coding: utf-8

from flask import Blueprint, request, render_template


app = Blueprint(__name__,
                "service",
                url_prefix="",
                static_url_path="",
                static_folder="app/static",
                template_folder="app/templates")


@app.route('/', methods=["GET", "POST"])
def index():
    template = "index.html"
    if request.method == "GET":
        return render_template(template, title=u"トップページ")


@app.route('/search', methods=["GET"])
def search():
    print request.args
    return "test"
