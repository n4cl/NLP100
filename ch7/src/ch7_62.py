# coding: utf-8

"""
62. KVS内の反復処理
60で構築したデータベースを用い，活動場所が「Japan」となっているアーティスト数を求めよ．
"""

from redis import StrictRedis
from ConfigReader import RedisConfig


def main():
    cnt = 0
    path = "./config.ini"
    redis_config = RedisConfig(path)
    host, port, db = redis_config.read_config()
    r = StrictRedis(host=host, port=port, db=db)
    for key in r.keys():
        if r.get(key) == "Japan":
            cnt += 1

    print cnt

if __name__ == '__main__':
    main()
