# coding: utf-8

"""
61. KVSの検索
60で構築したデータベースを用い，特定の（指定された）アーティストの活動場所を取得せよ．
"""

from redis import StrictRedis
from sys import argv


def main(name):

    r = StrictRedis(host='localhost', port=6379, db=0)

    # Redisから取得
    artist_name = r.get(name)

    if artist_name:
        print artist_name
    else:
        print u"データベースに存在しません"

if __name__ == '__main__':
    if len(argv) == 2:
        main(argv[1])
    else:
        print u"1つのアーティストを名を引数としてください"