# encoding: utf-8

"""
16. ファイルをN分割する
自然数Nをコマンドライン引数などの手段で受け取り，入力のファイルを行単位でN分割せよ．同様の処理をsplitコマンドで実現せよ．
"""

import sys

def split(file_path, line_number):

    # 1以上の整数のみ受け付ける
    if not line_number.isdigit(): return
    number = int(line_number)

    if number < 1: return

    with open(file_path, "r") as file:
        lines = file.readlines()
        line_count = len(lines)

        # 割り切れない場合は、余りの分をループさせる
        if line_count % number:
            split_count = line_count / number + 1
        else:
            split_count = line_count / number

        # ファイルを生成しながら、指定行だけ書き込む
        j = 0
        for i in range(0, split_count):
            with open("output" + str(i), "w") as split_file:

                # 分割した行ごとの最終行に改行コードが残ってしまうので削除
                split_file.write("\n".join([line.replace("\n", "") for line in lines[j:j + number]]))
            j += number

if __name__ == '__main__':

    if len(sys.argv[1:]) == 0:
        split("hightemp.txt", "10")
    elif len(sys.argv[1:]) == 1:
        split("hightemp.txt", sys.argv[1])
