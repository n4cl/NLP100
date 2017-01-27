# encoding: utf-8

"""
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""

from ch5_41 import analyze_dependency_structure


def ch5_42():
    sentences = analyze_dependency_structure("neko.txt.cabocha")

    # 文ごとに、係り元と係り先の組み合わせを表示
    for sentence in sentences:
        relation = []
        for i, c in enumerate(sentence):
            relation.append(c.get_chunk())
            for src in c.srcs:
                print relation[src] + relation[i]

if __name__ == '__main__':
    ch5_42()
