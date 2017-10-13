# encoding: utf-8

"""
13. col1.txtとcol2.txtをマージ
12で作ったcol1.txtとcol2.txtを結合し，元のファイルの1列目と2列目をタブ区切りで並べたテキストファイルを作成せよ．
確認にはpasteコマンドを用いよ．
"""


def marge(text1, text2):

    # 一行ごとに結合
    col_text = [line1.replace("\n", "") + "\t" + line2.replace("\n", "") for line1, line2 in zip(text1, text2)]
    return "\n".join(col_text)


def main():

    with open("col1.txt", "r") as col1, open("col2.txt", "r") as col2:

        # テキストを行単位で全て読み込み
        text1 = col1.readlines()
        text2 = col2.readlines()

        t = marge(text1, text2)

    with open("col1_col2.txt", "w") as f:
        f.write(t)


if __name__ == '__main__':
    main()
