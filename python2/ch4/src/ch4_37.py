# encoding: utf-8

"""
37. 頻度上位10語
出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
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

    words = [word.surface for word in mapping
             if not word.surface in surface
             and word.pos != pos
             and word.pos1 != pos1]

    return words


def main():
    with open("neko.txt", "r") as f:
        text = f.read()

    # 形態素解析処理
    mapping = map_morpheme(text)

    # 名詞のみを抽出
    words = extract_noun(mapping)

    # 名詞のカウント
    label = []
    count = []
    counter = Counter(words)
    for word, cnt in counter.most_common(10):
        label.append(word)
        count.append(cnt)

    # グラフ出力用に加工
    lebel = np.array(label)
    count = np.array(count)
    x_len = np.arange(len(lebel))

    # 日本語を利用するために、フォントを指定
    fp = FontProperties(fname="/Library/Fonts/Osaka.ttf")

    plt.title(u"頻度上位10語", fontproperties=fp)
    plt.ylabel(u"出現回数", fontproperties=fp)
    plt.xlabel(u"名詞", fontproperties=fp)

    # x軸にラベルを対応付ける
    plt.xticks(x_len, label, fontproperties=fp)

    plt.bar(x_len, count, align="center")
    plt.show()

if __name__ == '__main__':
    main()
