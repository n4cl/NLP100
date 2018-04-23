# coding: utf-8

"""
70. データの入手・整形
文に関する極性分析の正解データを用い，以下の要領で正解データ（sentiment.txt）を作成せよ．

rt-polarity.posの各行の先頭に"+1 "という文字列を追加する（極性ラベル"+1"とスペースに続けて肯定的な文の内容が続く）
rt-polarity.negの各行の先頭に"-1 "という文字列を追加する（極性ラベル"-1"とスペースに続けて否定的な文の内容が続く）
上述1と2の内容を結合（concatenate）し，行をランダムに並び替える
sentiment.txtを作成したら，正例（肯定的な文）の数と負例（否定的な文）の数を確認せよ．
"""

from random import shuffle


def main():
    with open("rt-polaritydata/rt-polarity.pos", 'r') as _file:
        pos = ["+1 " + line for line in _file.readlines()]

    with open("rt-polaritydata/rt-polarity.neg", 'r') as _file:
        neg = ["-1 " + line for line in _file.readlines()]

    sentence = []
    sentence.extend(pos)
    sentence.extend(neg)
    shuffle(sentence)

    with open("sentiment.txt", 'w') as _file:
        for line in sentence:
            _file.write(line)


if __name__ == '__main__':
    main()
