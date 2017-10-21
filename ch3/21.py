# encoding: utf-8

"""
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．
"""

from re import search


def extract_category():
    row = []
    with open("uk.txt", "r") as f:
        for i in f:
            if search("\[Category:.*\]", i):
                row.append(i)

    return row


def main():
    text = extract_category()
    print "".join(text)

if __name__ == '__main__':
    main()
