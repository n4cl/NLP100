# coding: utf-8

"""
67. 複数のドキュメントの取得
特定の（指定した）別名を持つアーティストを検索せよ．
"""

from sys import argv
from pymongo import MongoClient
from ConfigReader import MongoDBConfig


def search_artist_name(parm):

    query = parm
    query["aliases"] = {"$exists": "false"}

    path = "./config.ini"
    mongodb_config = MongoDBConfig(path)
    host, port = mongodb_config.read_config()
    port = int(port)

    # MongoDBからパラメータより検索
    client = MongoClient(host, port)
    db = client.local
    collection = db.artist

    return collection.find(query)


def main(parm):
    artist = search_artist_name(parm)

    for i in artist:
        print i

if __name__ == '__main__':
    main({"name": argv[1]})
