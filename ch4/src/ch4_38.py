# encoding: utf-8

"""
38. ヒストグラム
単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""

from ch4_30 import map_morpheme
from collections import Counter

import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def extract_noun(mapping):
    """ 名詞の抽出 """

    # 除外対象
    surface = [u"、", u"。", u"「", u"」", u"　"]
    pos = u"接頭詞"
    pos1 = u"接尾"

    words = [word["surface"] for word in mapping
             if not word["surface"] in surface
             and word["pos"] != pos
             and word["pos1"] != pos1]

    return words


def main():
    with open("neko.txt", "r") as f:
        text = f.read()

    # 形態素解析処理
    mapping = map_morpheme(text)

    # 名詞のみを抽出
    words = extract_noun(mapping)

    # 名詞の数をカウント
    counter = Counter(words)

    # カウント結果のみ取得
    word_count = [cnt for cnt in counter.values()]

    # 日本語を利用するために、フォントを指定
    fp = FontProperties(fname="/Library/Fonts/Osaka.ttf")

    plt.title(u"単語の出現頻度", fontproperties=fp)
    plt.ylabel(u"出現頻度をとる単語の種類数", fontproperties=fp)
    plt.xlabel(u"出現頻度", fontproperties=fp)
    plt.hist(word_count, bins=100, range=(0, 100))
    plt.show()

if __name__ == '__main__':
    main()
