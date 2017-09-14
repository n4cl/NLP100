# encoding: utf-8

"""
05. n-gram
与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．この関数を用い，
"I am an NLPer"という文から単語bi-gram，文字bi-gramを得よ．
"""


def n_gram(n, words):
    count = len(words) - n + 1
    return [words[i:i + n] for i in range(0, count)]

sentence = "I am an NLPer"
sentence = sentence.split()

print n_gram(n=2, words=sentence)
