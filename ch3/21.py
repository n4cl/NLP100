# encoding: utf-8

"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""

from re import search


def extract_category():
    row = []
    with open("uk.txt", "r") as file:
        for i in file:
            if search("\[Category:.*\]", i):
                row.append(i)

    return row

if __name__ == '__main__':
    text = extract_category()
    print "".join(text)
