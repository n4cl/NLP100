# coding: utf-8

"""
72. 素性抽出
極性分析に有用そうな素性を各自で設計し，学習データから素性を抽出せよ．素性としては，レビューからストップワードを除去し，各単語をステミング処理したものが最低限のベースラインとなるであろう．
"""

from nltk import PorterStemmer
from ch8_71 import has_stop_list


def main():
    with open("sentiment.txt", 'r') as _file:
        stemmer = PorterStemmer()
        features = []

        for words in _file:
            feature = []
            is_sentence = True

            # 極性ラベルを除外
            for word in words.split()[1:]:
                try:
                    word = word.decode("utf-8")
                    if word not in [".", ",", ":", "?", "!"] \
                            and not has_stop_list(word):

                        feature.append(stemmer.stem(word))
                except UnicodeDecodeError:
                    # 文字化けは無視する
                    is_sentence = False
                    break

            if is_sentence:
                features.append(feature)

    return features


if __name__ == '__main__':
    for feature in main():
        print feature
