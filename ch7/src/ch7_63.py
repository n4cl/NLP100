# coding: utf-8

"""
63. オブジェクトを値に格納したKVS
KVSを用い，アーティスト名（name）からタグと被タグ数（タグ付けされた回数）のリストを検索するためのデータベースを構築せよ．
さらに，ここで構築したデータベースを用い，アーティスト名からタグと被タグ数を検索せよ．
"""

from sys import argv
from redis import StrictRedis
from json import loads


def build_db():
    json_data = []
    with open("artist.json", 'r') as _file:
        for line in _file.readlines():
            # json stringをdic型に変換
            json_data.append(loads(line))

    r = StrictRedis(host='localhost', port=6379, db=1)

    # 接続しているDBを全消し
    r.flushdb()

    # Redisに登録
    for dic in json_data:
        if "tags" in dic:
            for tag in dic["tags"]:

                # ユニークID + アーティスト名, 被タグ数_タグのリストの組み合わせ
                r.sadd(str(dic["id"]) + "_" + dic["name"],
                       str(tag["count"]) + "_" + tag["value"])


def search_db(name):
    r = StrictRedis(host='localhost', port=6379, db=1)

    # Redisから取得
    artist_name_list = r.keys("*_" + name)

    if artist_name_list:
        for artist_name in artist_name_list:
            _id = artist_name.split("_")[:1][0]
            _name = "".join(artist_name.split("_")[1:])

            print u"ID:{} アーティスト名:{}".format(_id, _name)

            for tag in r.smembers(artist_name):
                tag_cnt = tag.split("_")[:1][0]
                tag_name = "".join(tag.split("_")[1:])
                print u"タグ:{} 被タグ数:{}".format(tag_name, tag_cnt)

    else:
        print u"データベースに存在しません"


def main(parm):
    if parm[1] == "build":
        build_db()
    elif parm[1] == "search":
        search_db(parm[2])

if __name__ == '__main__':
    main(argv)
