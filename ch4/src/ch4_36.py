# encoding: utf-8

"""
36. 単語の出現頻度
文章中に出現する単語とその出現頻度を求め，出現頻度の高い順に並べよ．
"""

from ch4_30 import map_morpheme
from collections import Counter


def main():
    with open("neko.txt", "r") as f:
        text = f.read()

    # 形態素解析処理
    mapping = map_morpheme(text)

    # 除外リスト
    surface = [u"、", u"。", u"「", u"」", u"　"]
    pos = u"接頭詞"
    pos1 = u"接尾"

    words = [word["surface"] for word in mapping
             if not word["surface"] in surface
             and word["pos"] != pos
             and word["pos1"] != pos1
             ]

    counter = Counter(words)
    for word, cnt in counter.most_common():
        print word, cnt


if __name__ == '__main__':
    main()
