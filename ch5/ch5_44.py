# encoding: utf-8

"""
44. 係り受け木の可視化
与えられた文の係り受け木を有向グラフとして可視化せよ．可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

import sys
import pydot
from ch5_41 import analyze_dependency_structure
from ch5_42 import create_relations

# pydotでマルチバイト文字を利用するためにデフォルトエンコーディングを変更
reload(sys)
sys.setdefaultencoding('utf-8')


def create_graph(edges, seq):

    graph = pydot.graph_from_edges(edge_list=edges, directed=True)

    # フォント設定
    n = pydot.Node("node")
    n.fontname = "Osaka.ttf"
    n.fontsize = 9
    graph.add_node(n)

    # グラフを出力
    graph.write_png("graph/graph_from_edges_dot_" + str(seq) + ".png", prog="dot")


if __name__ == '__main__':
    r = analyze_dependency_structure("neko.txt.cabocha")
    relations = create_relations(r)
    seq = 0
    for relation in relations:
        create_graph(relation, seq)
        seq += 1
