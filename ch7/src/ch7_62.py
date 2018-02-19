# coding: utf-8

"""
62. KVS内の反復処理
60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
"""

from redis import StrictRedis


def main():
    cnt = 0
    r = StrictRedis(host='localhost', port=6379, db=0)
    for key in r.keys():
        if r.get(key) == "Japan":
            cnt += 1

    print cnt

if __name__ == '__main__':
    main()
