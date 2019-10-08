# coding: utf-8

"""
60. KVSの構築
Key-Value-Store (KVS) を用い，アーティスト名（name）から活動場所（area）を検索するためのデータベースを構築せよ．
"""

from redis import StrictRedis
from json import loads
from ConfigReader import RedisConfig


def main():
    json_data = []
    with open("artist.json", 'r') as _file:
        for line in _file.readlines():
            # json stringをdic型に変換
            json_data.append(loads(line))

    path = "./config.ini"
    redis_config = RedisConfig(path)
    host, port, db = redis_config.read_config()

    r = StrictRedis(host=host, port=port, db=db)

    # 接続しているDBを全消し
    r.flushdb()

    # Redisに登録
    for dic in json_data:
        if "area" in dic:
            r.set(str(dic["id"]) + "_" + dic["name"], dic["area"])


if __name__ == '__main__':
    main()
