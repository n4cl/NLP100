# encoding: utf-8

"""
10. 行数のカウント
行数をカウントせよ．確認にはwcコマンドを用いよ．
"""


def count_line(file_path):
    with open(file_path, "r") as file:
        number = sum([1 for line in file])
        return number

if __name__ == '__main__':
    print count_line("hightemp.txt")
