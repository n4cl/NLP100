# coding: utf-8

"""
64. MongoDBの構築
アーティスト情報（artist.json.gz）をデータベースに登録せよ．
さらに，次のフィールドでインデックスを作成せよ: name, aliases.name, tags.value, rating.value
"""

from json import loads
from pymongo import MongoClient


def main():

    # jsonファイルの読み込み
    json_data = []
    with open("artist.json", 'r') as _file:
        for line in _file.readlines():
            # json stringをdic型に変換
            json_data.append(loads(line))

    # MongoDBへ登録
    client = MongoClient("localhost", 27017)
    db = client.local
    collection = db.artist

    # 必要なデータを抽出しながら登録
    for artist in json_data:
        _aliases = []
        _tags = []
        _rating = None

        if "aliases" in artist:
            for alias in artist["aliases"]:
                _aliases.append(alias["name"])
        else:
            _aliases = None

        if "tags" in artist:
            for tag in artist["tags"]:
                _tags.append(tag["value"])
        else:
            _tags = None

        if "rating" in artist:
            _rating = artist["rating"]["value"]

        collection.insert({"name": artist["name"],
                           "aliases": _aliases,
                           "tags": _tags,
                           "rating": _rating})

if __name__ == '__main__':
    main()
