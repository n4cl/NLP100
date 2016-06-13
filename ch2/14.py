# encoding: utf-8

"""
14. 先頭からN行を出力
自然数Nをコマンドライン引数などの手段で受け取り，入力のうち先頭のN行だけを表示せよ．確認にはheadコマンドを用いよ．
"""

import sys

def head(file_path, number):
    with open(file_path, "r") as file:

        # 最終行となる行に改行コードが入るため、一旦削除する
        head_text = [line.replace("\n", "") for line in file.readlines()[:number]]
        print "\n".join(head_text)

if __name__ == '__main__':

    if len(sys.argv[1:]) == 0:
        head("hightemp.txt", 5)
    elif len(sys.argv[1:]) == 1:
        arg = str(sys.argv[1])
        if arg.isdigit: head("hightemp.txt", int(sys.argv[1]))
