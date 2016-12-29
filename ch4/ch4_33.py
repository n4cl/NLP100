# encoding: utf-8

"""
33. サ変名詞
サ変接続の名詞をすべて抽出せよ．
"""

from ch4_30 import map_morpheme

if __name__ == '__main__':

    with open("neko.txt", "r") as file:
        text = file.read()

    # 形態素解析処理
    mapping = map_morpheme(text)

    # 割当結果を出力
    for m in mapping:
        if m["pos1"] == u"サ変接続": print m["surface"]
