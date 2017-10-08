# encoding: utf-8

"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""

with open("hightemp.txt", "r") as f:

    # テキストを行単位で全て読み込み
    text = f.readlines()

    # 列の抽出
    first_col = [line.split()[0] for line in text]
    second_col = [line.split()[1] for line in text]

    # 列要素の連結
    first_col = "\n".join(first_col)
    second_col = "\n".join(second_col)

    with open("col1.txt", "w") as col:
        col.write(first_col)

    with open("col2.txt", "w") as col:
        col.write(second_col)
