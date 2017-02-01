# encoding: utf-8

"""
43. 名詞を含む文節が動詞を含む文節に係るものを抽出
名詞を含む文節が，動詞を含む文節に係るとき，これらをタブ区切り形式で抽出せよ．ただし，句読点などの記号は出力しないようにせよ．
"""

from ch5_41 import analyze_dependency_structure


def ch5_43():
    sentences = analyze_dependency_structure("neko.txt.cabocha")

    # 文ごとに、係り元と係り先の組み合わせを表示
    for sentence in sentences:
        relation = []
        for i, chunk in enumerate(sentence):

            # 名詞、動詞を含むか判定
            chunk.has_part()
            relation.append(chunk)

            # 係り先となるか判定
            if not chunk.verb:
                continue

            # 名詞を含む文節が、動詞を含む文節に係る場合のみ出力
            for src in chunk.srcs:
                if relation[src].noun:
                    print relation[src].get_chunk() + "\t" + relation[i].get_chunk()


if __name__ == '__main__':
    ch5_43()
