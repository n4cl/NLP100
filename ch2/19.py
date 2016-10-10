# encoding: utf-8

"""
19. 各行の1コラム目の文字列の出現頻度を求め，出現頻度の高い順に並べる
各行の1列目の文字列の出現頻度を求め，その高い順に並べて表示せよ．確認にはcut, uniq, sortコマンドを用いよ．
"""

def sort(file_path):

    with open(file_path, "r") as file:
        lines = file.readlines()
        word_list = {}
        word_recode = {}

        # 1カラム目の文字列のカウントと1カラム目の文字列のレコード別辞書作成
        line_list = [line.split() for line in lines]
        for line in line_list:
            if line[0] not in word_list:
                word_list[line[0]] = 0
                word_recode[line[0]] = [line]
            else:
                word_recode[line[0]].append(line)
            word_list[line[0]] += 1

    # 降順で出力
    item = []
    for i, j in sorted(word_list.items(), key=lambda x:x[1], reverse=True):
        for k in word_recode[i]:
            item.append("\t".join(k))
    print "\n".join(item)

if __name__ == '__main__':
    sort("hightemp.txt")
