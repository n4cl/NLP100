# encoding: utf-8

"""
15. 末尾のN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち末尾のN行だけを表示せよ．確認にはtailコマンドを用いよ．
"""

import sys


def head(file_path, number):

    # 1以上の整数のみ受け付ける
    if not number.isdigit():
        return
    number = int(number)

    if number < 1:
        return

    with open(file_path, "r") as f:
        lines = f.readlines()

        # 最終行から必要な行数を抽出
        head_text = [line.replace("\n", "")
                     for line in lines[len(lines) - number:]]
        print "\n".join(head_text)


if __name__ == '__main__':

    if len(sys.argv[1:]) == 0:
        head("hightemp.txt", "5")
    elif len(sys.argv[1:]) == 1:
        head("hightemp.txt", sys.argv[1])
