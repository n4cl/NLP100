# encoding: utf-8

"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
"""

from re import search


def extract_media():
    row = []
    with open("uk.txt", "r") as file:
        for i in file:
            media = search("(File|ファイル):(.*?)\|", i)
            if media:
                row.append(media.group(2))

    return row

if __name__ == '__main__':
    text = extract_media()
    print "\n".join(text)
