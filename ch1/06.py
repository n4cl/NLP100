# encoding: utf-8

"""
06. 集合
"paraparaparadise"と"paragraph"に含まれる文字bi-gramの集合を，
それぞれ, XとYとして求め，XとYの和集合，積集合，差集合を求めよ．
さらに，'se'というbi-gramがXおよびYに含まれるかどうかを調べよ．
"""


def n_gram(n, words):
    count = len(words) - n + 1
    return [words[i:i + n] for i in range(0, count)]


word_1 = "paraparaparadise"
word_2 = "paragraph"

x = set(n_gram(2, word_1))
y = set(n_gram(2, word_2))

print u"Xの集合:" + str(list(x))
print u"Yの集合:" + str(list(y))

print u"XとYの和集合:" + str(list(x | y))
print u"XとYの積集合:" + str(list(x & y))
print u"XとYの差集合:" + str(list(x - y))

if 'se' in x:
    print u"seがxの中に含まれる"
else:
    print u"seがxの中に含まれない"

if 'se' in y:
    print u"seがyの中に含まれる"
else:
    print u"seがyの中に含まれない"
