# coding: utf-8

"""
65. MongoDBの検索
MongoDBのインタラクティブシェルを用いて，"Queen"というアーティストに関する情報を取得せよ．
さらに，これと同様の処理を行うプログラムを実装せよ．
"""

from pymongo import MongoClient
from ConfigReader import MongoDBConfig


def search_artist_info(parm):

    path = "./config.ini"
    mongodb_config = MongoDBConfig(path)
    host, port = mongodb_config.read_config()
    port = int(port)

    # MongoDBからパラメータより検索
    client = MongoClient(host, port)
    db = client.local
    collection = db.artist

    return collection.find(parm)


def main(parm):
    artist = search_artist_info(parm)

    for i in artist:
        print i

if __name__ == '__main__':
    main({"name": "Queen"})
