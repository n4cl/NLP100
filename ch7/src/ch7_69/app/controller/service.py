# coding: utf-8
from json import dumps
from flask import Blueprint, request, render_template, Response
from app.model.search import ArtistDBClient

"""
引数であるstatic_folder, template_folderは、
flaskサーバーを起動したフォルダの位置で適宜変更する
"""
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
    name = request.args.get("name")
    alias = request.args.get("alias")
    tag = request.args.get("tag")

    client = ArtistDBClient(name=name, alias=alias, tag=tag)
    client.connect_db()
    artist = []

    # json化するときに邪魔なので、Object IDを削除する
    for i in client.fetch_artist():
        i.pop("_id")
        artist.append(i)

    res = {"artist": artist}

    # Flaskのjsonifyはlistを扱えないので以下のように返している
    return Response(dumps(res), mimetype="application/json")
