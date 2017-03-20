# encoding: utf-8

"""
夏目漱石の小説『吾輩は猫である』の文章（neko.txt）をCaboChaを使って係り受け解析し，その結果をneko.txt.cabochaというファイルに保存せよ．
このファイルを用いて，以下の問に対応するプログラムを実装せよ．
"""

import CaboCha


def analyze_dependency_structure(line):
    """ 係り受け解析を実行する
    :param line: 行テキスト
    :return : 行テキストを係り受け解析した結果の文字列
    """
    c = CaboCha.Parser()
    res = c.parse(line)
    return res.toString(CaboCha.FORMAT_LATTICE)


def main():
    with open("neko.txt", "r") as f:
        analysis_result = []

        for text in f:
            text = text.decode("utf-8")

            # 空行は無視
            if text != "\n":
                # 字下げ削除
                if text[0] == u"　":
                    text = text[1:]
                analysis_result.append(
                    analyze_dependency_structure(text.encode("utf-8")))

    with open("neko.txt.cabocha", "w") as f:
        f.write("".join(analysis_result))

if __name__ == '__main__':
    main()
