# encoding: utf-8

"""
17. １列目の文字列の異なり
1列目の文字列の種類（異なる文字列の集合）を求めよ．確認にはsort, uniqコマンドを用いよ．
"""


def find_word_set(file_path):

    words = []

    # ファイルから1列目を取得
    with open(file_path, "r") as f:
        lines = f.readlines()
        words += [line.split()[0] for line in lines]

    # 重複単語を削除して単語を出力
    for word in set(words):
        print word

if __name__ == '__main__':
    find_word_set("hightemp.txt")
