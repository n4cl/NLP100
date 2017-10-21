# encoding: utf-8

"""
25. テンプレートの抽出
記事中に含まれる「基礎情報」テンプレートのフィールド名と値を抽出し，辞書オブジェクトとして格納せよ．
"""

from re import search, split


def extract_basic_information():
    row = {}
    with open("uk.txt", "r") as f:
        text = f.read()
        text = search(r"\{\{基礎情報[\s\S]*?\n\}\}", text).group()
        text = split(r"\n[\|}]", text)
    for i in text[1:-1]:

        # 左辺と右辺に分離
        res = search(r"^(.*?)\s=\s(.*)", i)

        # 公式国名のためだけの前処理
        sp = i.split("<br/>\n")

        if len(sp) == 1:
            row[res.group(1)] = res.group(2)
        else:
            row[res.group(1)] = res.group(2) + "".join(sp[1:])

    return row

if __name__ == '__main__':
    print extract_basic_information()
