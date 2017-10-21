# encoding: utf-8

"""
24. ファイル参照の抽出
記事から参照されているメディアファイルをすべて抜き出せ．
"""

from re import search


def extract_media():
    row = []
    with open("uk.txt", "r") as f:
        for i in f:
            media = search("(File|ファイル):(.*?)\|", i)
            if media:
                row.append(media.group(2))

    return row


def main():
    text = extract_media()
    print "\n".join(text)

if __name__ == '__main__':
    main()
