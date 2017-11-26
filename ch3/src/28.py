# encoding: utf-8

"""
28. MediaWikiマークアップの除去
27の処理に加えて，テンプレートの値からMediaWikiマークアップを可能な限り除去し，国の基本情報を整形せよ．
"""

from re import search, split, sub


def remove_media_wiki_markup(text):
    text = sub(r"'{2,4}", r"", text)
    text = sub(r"\[{2}([^|\]]+?\|)*(.+?)\]{2}", r"\2", text)
    text = sub(r"\{{2}.+?\}{2}", "", text)
    text = sub(r"\n\*{1,2}", "", text)
    return text


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
            row[res.group(1)] = remove_media_wiki_markup(res.group(2))
        else:
            row[res.group(1)] = remove_media_wiki_markup(
                res.group(2) + "\n" + "\n".join(sp[1:]))

    return row

if __name__ == '__main__':
    for k, v in extract_basic_information().items():
        print "key: %s, value: %s" % (k, v)
