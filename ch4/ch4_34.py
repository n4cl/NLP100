# encoding: utf-8

"""
34. 「AのB」
2つの名詞が「の」で連結されている名詞句を抽出せよ．
"""

from ch4_30 import map_morpheme

if __name__ == '__main__':

    with open("neko.txt", "r") as file:
        text = file.read()

    # 形態素解析処理
    mapping = map_morpheme(text)

    for i, m in enumerate(mapping):
        if m["surface"] == "の" and m["pos"] == "助詞":

            # 付加部の取得
            begin = 1
            adj = []
            while True:
                if mapping[i-begin]["pos"] == "名詞":
                    adj.append(mapping[i-begin]["surface"])
                    begin = begin + 1
                elif mapping[i-begin]["pos1"] == "格助詞":
                    adj.append(mapping[i-begin]["surface"])
                    begin = begin + 1
                else:
                    break

            # 主要部の取得
            end = 1
            main = []
            while True:
                if mapping[i+end]["pos"] == "名詞":
                    main.append(mapping[i+end]["surface"])
                    end = end + 1
                else:
                    break

            # 名詞句の出力
            if begin != 1 and end != 1: print "".join(adj) + m["surface"] + "".join(main)
