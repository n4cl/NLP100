# encoding: utf-8

"""
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""

from re import search, split
from urllib2 import urlopen
from json import load

def extract_basic_information():
    row = {}
    with open("uk.txt", "r") as file:
        text = file.read()
        text = search(r"\{\{基礎情報[\s\S]*?\n\}\}",text).group()
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
    info = extract_basic_information()
    url = "https://www.mediawiki.org/w/api.php"
    parameters = "?action=query&titles=File:Flag%20of%20the%20United%20Kingdom.svg&prop=imageinfo&iiprop=url&format=json"
    response = load(urlopen(url + parameters))
    print response["query"]["pages"]["-1"]["imageinfo"][0]["url"]
