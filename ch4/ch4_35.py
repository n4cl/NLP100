# encoding: utf-8

"""
35. 名詞の連接
名詞の連接（連続して出現する名詞）を最長一致で抽出せよ．
"""

from ch4_30 import map_morpheme


def extract_nouns(mapping):
    noun = []
    nouns = []
    for i, m in enumerate(mapping):

        # 連続する名詞を抽出する
        if m["pos"] == u"名詞":
            noun.append(m["surface"])
        else:
            if len(noun) > 1:
                nouns.append("".join(noun))
            noun = []
    return nouns

if __name__ == '__main__':

    with open("neko.txt", "r") as file:
        text = file.read()

    # 形態素解析処理
    mapping = map_morpheme(text)

    # 名詞の連接を取得
    nouns = extract_nouns(mapping)

    for noun in nouns:
        print noun
