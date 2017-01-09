# encoding: utf-8

"""
40. 係り受け解析結果の読み込み（形態素）
形態素を表すクラスMorphを実装せよ．
このクラスは表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をメンバ変数に持つこととする．
さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""

class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1

    def enc(self, surface, base, pos, pos1):
        return

    def __repr__(self):
        return u"Morph('{}'"\
                   u", '{}'" \
                   u", '{}'" \
                   u", '{}')"\
               .format(self.surface
                     , self.base
                     , self.pos
                     , self.pos1).encode("utf-8")

    def __str__(self):
        return u"Morph('surface':'{}'" \
                   u", 'base':'{}'" \
                   u", 'pos':'{}'" \
                   u", 'pos1':'{}')"\
               .format(self.surface
                     , self.base
                     , self.pos
                     , self.pos1).encode("utf-8")

with open("neko.txt.cabocha", "r") as file:
    text = file.readline()
    sentence = []
    morph = []

    while text:
        text = text.decode("utf-8")

        # 形態素列の判定
        if text.find(u"\t") != -1:
            surface, elements = text.split(u"\t")
            elements = elements.split(u",")
            m = Morph(surface, elements[6], elements[0], elements[1])
            morph.append(m)

            # 句点で文を区切る
            if surface == u"。":
                sentence.append(morph)
                morph = []

        text = file.readline()

# 3文目の形態素を出力
for m in sentence[2]:
    print m.surface
