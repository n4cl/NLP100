# coding: utf-8

"""
68. ソート
"dance"というタグを付与されたアーティストの中でレーティングの投票数が多いアーティスト・トップ10を求めよ．
"""

from pymongo import MongoClient
import config
#import HOST, PORT


def search_top_artist():

    # MongoDBからパラメータより検索
    client = MongoClient(HOST, PORT)
    db = client.local
    collection = db.artist

    # 問い合わせ内容
    query = {"tags": {"$elemMatch": {"value": "dance"}}}
    order_key = "rating.count"
    order_value = -1
    top = 10

    return collection.find(query).sort(order_key, order_value).limit(top)


def main():
    artist = search_top_artist()

    for i in artist:
        print i

if __name__ == '__main__':
    main()
