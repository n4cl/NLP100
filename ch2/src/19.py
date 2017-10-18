# encoding: utf-8

"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""
from collections import Counter


def count(file_path):

    with open(file_path, "r") as f:
        lines = f.readlines()

        # 1カラム目を取得
        column = [line.split()[0] for line in lines]
        column.sort()

    # 文字列のカウント
    count_result = Counter(column)

    # 出現頻度が高い順に出力
    for k, v in count_result.most_common():
        print v, k


if __name__ == '__main__':
    count("hightemp.txt")
