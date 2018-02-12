# coding: utf-8

"""
30. 形態素解析結果の読み込み
形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import MeCab


class Morpheme(object):
    def __init__(self, surface, base, pos, pos1):
        """
        :param surface: 表層系
        :param base: 基本形
        :param pos: 品詞
        :param pos1: 品詞細分類1
        """
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def __str__(self):
        return u"表層形:{}\n" \
               u"基本形:{}\n" \
               u"品詞:{}\n" \
               u"品詞細分類1:{}\n".format(self._surface
                                       , self._base
                                       , self._pos
                                       , self._pos1).encode("utf-8")


def map_morpheme(text):
    mapping = []

    m = MeCab.Tagger("mecabrc")
    for line in m.parse(text).split("\n"):
        if line == "EOS":
            break

        # 形態素解析結果を分割する
        surface, fields = line.split("\t")
        f = fields.split(",")
        morpheme = Morpheme(surface.decode("utf-8")
                          , f[6].decode("utf-8")
                          , f[0].decode("utf-8")
                          , f[1].decode("utf-8")
                            )
        mapping.append(morpheme)
    return mapping


def main():
    with open("neko.txt", "r") as f:
        text = f.read()

    mapping = map_morpheme(text)

    # 割当結果を出力
    for m in mapping:
        print m.surface, m.base, m.pos, m.pos1

if __name__ == '__main__':
    main()
