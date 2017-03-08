# encoding: utf-8

"""
42. 係り元と係り先の文節の表示
係り元の文節と係り先の文節のテキストをタブ区切り形式ですべて抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""

from ch5_41 import analyze_dependency_structure


def create_relations(sentences):

    # 文ごとに、係り元と係り先の組み合わせを取得
    s = []
    for sentence in sentences:
        s.append(create_relation(sentence))

    return s


def create_relation(sentence):

    # 文の係り元と係り先の組み合わせを取得
    relation = []
    relations = []
    for i, c in enumerate(sentence):
        relation.append(c.get_chunk())
        for src in c.srcs:
            relations.append([relation[src], relation[i]])

    return relations

if __name__ == '__main__':
    sentences = analyze_dependency_structure("neko.txt.cabocha")
    relations = create_relations(sentences)
    for relation in relations:
        for r in relation:
            print "\t".join(r)
