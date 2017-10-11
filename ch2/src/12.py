# encoding: utf-8

"""
12. 1列目をcol1.txtに，2列目をcol2.txtに保存
各行の1列目だけを抜き出したものをcol1.txtに，2列目だけを抜き出したものをcol2.txtとしてファイルに保存せよ．確認にはcutコマンドを用いよ．
"""


def select_column(text, number):

    # 列の抽出
    column = [line.split()[number] for line in text]

    # 列要素の連結
    return "\n".join(column)


def main():
    with open("hightemp.txt", "r") as f:
        # テキストを行単位で全て読み込み
        text = f.readlines()

        # 1列目
        first = select_column(text, 0)

        # 2列目
        second = select_column(text, 1)

    with open("col1.txt", "w") as col1:
        col1.write(first)

    # 出力確認
    print u"1列目"
    print first
    print ""

    with open("col2.txt", "w") as col2:
        col2.write(second)

    # 出力確認
    print u"2列目"
    print second


if __name__ == '__main__':
    main()
