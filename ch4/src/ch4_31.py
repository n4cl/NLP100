# encoding: utf-8

"""
31. 動詞
動詞の表層形をすべて抽出せよ．
"""

from ch4_30 import map_morpheme


def main():
    with open("neko.txt", "r") as f:
        text = f.read()

    # 形態素解析処理
    mapping = map_morpheme(text)

    # 割当結果を出力
    for m in mapping:
        if m["pos"] == u"動詞":
            print m["surface"]

if __name__ == '__main__':
    main()
