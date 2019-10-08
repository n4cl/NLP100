# coding: utf-8

"""
61. KVSの検索
60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．
"""

from redis import StrictRedis
from sys import argv
from ConfigReader import RedisConfig


def main(name):

    path = "./config.ini"
    redis_config = RedisConfig(path)
    host, port, db = redis_config.read_config()

    r = StrictRedis(host=host, port=port, db=db)

    # Redisから取得
    artist_name_list = r.keys("*_" + name)

    if artist_name_list:
        for artist_name in artist_name_list:
            _id = artist_name.split("_")[:1][0]
            _name = "".join(artist_name.split("_")[1:])
            print u"ID:{} アーティスト名:{} 活動場所:{}".format(_id, _name, r.get(artist_name))
    else:
        print u"データベースに存在しません"

if __name__ == '__main__':

    # 問題的はユニークな値で検索するのが正解な気がする
    if len(argv) == 2:
        main(argv[1])
    else:
        print u"1つのアーティストを名を引数としてください"