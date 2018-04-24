# coding: utf-8

"""
71. ストップワード
英語のストップワードのリスト（ストップリスト）を適当に作成せよ．
さらに，引数に与えられた単語（文字列）がストップリストに含まれている場合は真，それ以外は偽を返す関数を実装せよ．
さらに，その関数に対するテストを記述せよ．
"""

"""
ストップワードはOracle Textを参照
https://docs.oracle.com/cd/E16338_01/text.112/b61357/astopsup.htm#i634475
"""

STOP_LIST = [
    "a",
    "did",
    "in",
    "only",
    "then",
    "where",
    "all",
    "do",
    "into",
    "onto",
    "there",
    "whether",
    "almost",
    "does",
    "is",
    "and",
    "therefore",
    "which",
    "also",
    "either",
    "it",
    "our",
    "these",
    "while",
    "although",
    "for",
    "its",
    "ours",
    "they",
    "who",
    "an",
    "from",
    "just",
    "s",
    "this",
    "whose",
    "or",
    "had",
    "ll",
    "shall",
    "those",
    "why",
    "any",
    "has",
    "me",
    "she",
    "though",
    "will",
    "are",
    "have",
    "might",
    "should",
    "through",
    "with",
    "as",
    "having",
    "Mr",
    "since",
    "thus",
    "would",
    "at",
    "he",
    "Mrs",
    "so",
    "to",
    "yet",
    "be",
    "her",
    "Ms",
    "some",
    "too",
    "you",
    "because",
    "here",
    "my",
    "still",
    "until",
    "your",
    "been",
    "hers",
    "no",
    "such",
    "ve",
    "yours",
    "both",
    "him",
    "non",
    "t",
    "very",
    "but",
    "his",
    "nor",
    "than",
    "was",
    "by",
    "how",
    "not",
    "that",
    "we",
    "can",
    "however",
    "of",
    "the",
    "were",
    "could",
    "i",
    "on",
    "their",
    "what",
    "d",
    "if",
    "one",
    "them",
    "when"
]


def has_stop_list(sentence):
    # 単語毎に区切ってSTOP LISTに含まれるかチェックする
    for word in sentence.split():
        if word in STOP_LIST:
            return True

    return False


if __name__ == '__main__':
    assert has_stop_list("vipoignant and funny .") == True
    assert has_stop_list("good looks.") == False
