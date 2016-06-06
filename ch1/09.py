# encoding: utf-8

"""
09. Typoglycemia
スペースで区切られた単語列に対して，各単語の先頭と末尾の文字は残し，それ以外の文字の順序をランダムに並び替えるプログラムを作成せよ．
ただし，長さが４以下の単語は並び替えないこととする．
適当な英語の文（例えば"I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."）を与え，
その実行結果を確認せよ．
"""

import random

sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
sentence = sentence.split()

random_text = []

for word in sentence:
    length = len(word)

    # 単語列の並び替え
    if length > 4:

        # 先頭と末尾のみ残して、間のインデックスの順番をランダムに変更
        last_index = length - 1
        sort_number = range(1, last_index)
        random.shuffle(sort_number)
        sort_number = [0] + sort_number + [last_index]
        random_word = ""

        for i in sort_number:
            random_word += word[i]

        random_text.append(random_word)

    else:
        random_text.append(word)

print " ".join(random_text)
