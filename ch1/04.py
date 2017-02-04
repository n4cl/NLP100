# encoding: utf-8

"""
04. 元素記号
"Hi He Lied Because Boron Could Not Oxidize Fluorine." \
" New Nations Might Also Sign Peace Security Clause." \
" Arthur King Can."
という文を単語に分解し，1, 5, 6, 7, 8, 9, 15, 16, 19番目の単語は先頭の1文字，それ以外の単語は先頭に2文字を取り出し，
取り出した文字列から単語の位置（先頭から何番目の単語か）への連想配列（辞書型もしくはマップ型）を作成せよ．
"""

sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine." \
           " New Nations Might Also Sign Peace Security Clause." \
           " Arthur King Can."
number = [1, 5, 6, 7, 8, 9, 15, 16, 19]
sentence = sentence.replace(".", "")
words = sentence.split()
dic = {}

for index, word in enumerate(words):
    if index + 1 in number:
        pos = 1
    else:
        pos = 2
    dic.update({index + 1: word[:pos]})

print dic
