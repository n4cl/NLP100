# encoding: utf-8

"""
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
"""

from re import search

def extract_category_value():
    row = []
    with open("uk.txt", "r") as file:
        for i in file:
            # 後方参照を利用して、マッチした一部を抽出
            category = search("\[\[Category:(.*)\]\]",i)
            if category: row.append(category.group(1))

    return row

if __name__ == '__main__':
    text = extract_category_value()
    print "\n".join(text)
