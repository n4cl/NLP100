# encoding: utf-8

"""
39. Zipfの法則
単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

from ch4_30 import map_morpheme
from collections import Counter

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

def extract_noun(mapping):
    """ 名詞の抽出 """

    # 除外対象
    surface = [u"、", u"。", u"「", u"」", u"　"]
    pos = u"接頭詞"
    pos1 = u"接尾"

    words = [word["surface"] for word in mapping \
             if not word["surface"] in surface \
             and word["pos"] != pos \
             and word["pos1"] != pos1]

    return words

if __name__ == '__main__':

    with open("neko.txt", "r") as file:
        text = file.read()

    # 形態素解析処理
    mapping = map_morpheme(text)

    # 名詞のみを抽出
    words = extract_noun(mapping)

    # 名詞の数をカウント
    counter = Counter(words)

    # カウント結果のみ取得
    word_count = [cnt for cnt in counter.values()]
    word_count.sort(reverse=True)

    # 順位生成
    rank = [i + 1 for i, count in enumerate(word_count)]

    # 日本語を利用するために、フォントを指定
    fp = FontProperties(fname="/Library/Fonts/Osaka.ttf")

    plt.title(u"Zipfの法則", fontproperties=fp)
    plt.ylabel(u"出現頻度", fontproperties=fp)
    plt.xlabel(u"出現頻度順位", fontproperties=fp)
    plt.xscale("log")
    plt.yscale("log")
    plt.plot(rank, word_count)
    plt.show()
