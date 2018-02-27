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

    collection.drop()

    # 必要なデータを抽出しながら登録
    for artist in json_data:
        collection.insert_one(artist)

    # インデックスの生成
    collection.create_index("name")
    collection.create_index("aliases")
    collection.create_index("tags")
    collection.create_index("rating")

if __name__ == '__main__':
    main()
