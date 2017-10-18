# encoding: utf-8

"""
29. 国旗画像のURLを取得する
テンプレートの内容を利用し，国旗画像のURLを取得せよ．
（ヒント: MediaWiki APIのimageinfoを呼び出して，ファイル参照をURLに変換すればよい）
"""

from urllib2 import urlopen
from json import load


def fetch_nationalflag_img():
    url = "https://www.mediawiki.org/w/api.php"
    parameters = "?action=query" \
                 "&titles=File:Flag%20of%20the%20United%20Kingdom.svg" \
                 "&prop=imageinfo&iiprop=url" \
                 "&format=json"
    response = load(urlopen(url + parameters))
    print response["query"]["pages"]["-1"]["imageinfo"][0]["url"]

if __name__ == '__main__':
    fetch_nationalflag_img()
