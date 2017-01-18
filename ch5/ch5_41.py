# encoding: utf-8

"""
41. 係り受け解析結果の読み込み（文節・係り受け）
40に加えて，文節を表すクラスChunkを実装せよ．このクラスは形態素（Morphオブジェクト）のリスト（morphs），
係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）をメンバ変数に持つこととする．
さらに，入力テキストのCaboChaの解析結果を読み込み，１文をChunkオブジェクトのリストとして表現し，8文目の文節の文字列と係り先を表示せよ．
第5章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

from ch5_40 import Morph

class Chunk(object):
    def __init__(self, morphs, dst, srcs):
        self.morphs = morphs
        self.dst = dst
        self.srcs = srcs

if __name__ == '__main__':
    with open("neko.txt.cabocha", "r") as file:
        chunk = None
        sentence = []
        chunks = []
        morph = []
        srcs = {}

        for line in file:
            line = line.decode("utf-8")

            # 文節情報
            if line[0] == u"*" and line.find(u"\t") == -1:

                if chunk:
                    chunk.morphs = morph
                    chunks.append(chunk)
                    morph = []

                phrase = line.split(u" ")

                # Dを削除
                dst = int(phrase[2][:-1])

                # 係り元と係り先の組み合わせ
                src = int(phrase[1])
                srcs[src] = int(phrase[2][:-1])

                # 係り先の判定
                s = []
                for k, v in srcs.items():
                    if src == v:
                        s.append(k)

                chunk = Chunk([], dst, s)

            # 形態素列の判定
            if line.find(u"\t") != -1:
                surface, elements = line.split(u"\t")
                elements = elements.split(u",")
                m = Morph(surface, elements[6], elements[0], elements[1])
                morph.append(m)

            # 文の終わり
            if line == u"EOS\n":
                chunk.morphs = morph
                chunks.append(chunk)
                sentence.append(chunks)

                # 次の文を入力するために初期化
                chunk = None
                chunks = []
                morph = []
                srcs = {}

    # 8文目の文節の文字列と係り先を表示
    for c in sentence[7]:
        chunk = [i.surface for i in c.morphs]
        chunk = "".join(chunk)
        print chunk, c.dst
