# encoding: utf-8

"""
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．
"""

import CaboCha

def analyze_dependency_structure(text):

    c = CaboCha.Parser()
    res = c.parse(text)
    return res.toString(CaboCha.FORMAT_LATTICE)

with open("neko.txt", "r") as file:
    text = file.read()

analysis_result = analyze_dependency_structure(text)

with open("neko.txt.cabocha", "w") as file:
    file.write(analysis_result)
