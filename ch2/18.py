# encoding: utf-8

"""
18. 各行を3コラム目の数値の降順にソート
各行を3コラム目の数値の逆順で整列せよ（注意: 各行の内容は変更せずに並び替えよ）．
確認にはsortコマンドを用いよ（この問題はコマンドで実行した時の結果と合わなくてもよい）．
"""


def sort(file_path):

    line_list = []
    with open(file_path, "r") as file:
        lines = file.readlines()

        # 各行を比較できるように、一行ごとにリスト化
        line_list += [line.split() for line in lines]

    # 挿入ソート
    for i in range(1, len(lines)):
        v = line_list[i]
        j = i - 1

        while j >= 0 and line_list[j][2] > v:
            line_list[j + 1] = line_list[j]
            j -= 1
        line_list[j + 1] = v

    # リスト化された行を再度元のtab区切りの形に戻す
    item = ["\t".join(items) for items in line_list]
    print "\n".join(item)

if __name__ == '__main__':
    sort("hightemp.txt")
