# encoding: utf-8

"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import MeCab

def map_morpheme(text):
    mapping = []

    m = MeCab.Tagger("mecabrc")
    for line in m.parse(text).split("\n"):
        if line == "EOS": break

        # 形態素解析結果を分割する
        surface, fields = line.split("\t")
        f = fields.split(",")
        t = {u"surface": surface.decode("utf-8")
           , u"base": f[6].decode("utf-8")
           , u"pos": f[0].decode("utf-8")
           , u"pos1": f[1].decode("utf-8")
             }
        mapping.append(t)

    return mapping

if __name__ == '__main__':

    with open("neko.txt", "r") as file:
        text = file.read()

    mapping = map_morpheme(text)

    # 割当結果を出力
    for m in mapping:
        print m["surface"], m["base"], m["pos"], m["pos1"]
