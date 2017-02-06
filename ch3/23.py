# encoding: utf-8

"""
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
"""

from re import search


def extract_section_level():
    row = []
    with open("uk.txt", "r") as file:
        for i in file:
            # .*? : 最小限のマッチ
            # .*  : =が複数あると、後尾の手前までマッチしてしまう
            section = search("^(\=+)\s?(.*?)\s?(\=+)$", i)
            # == : level 1 , === : level 2, ==== : level 3
            if section:
                row.append(section.group(2) + " " +
                           str(len(section.group(1)) - 1))

    return row

if __name__ == '__main__':
    text = extract_section_level()
    print "\n".join(text)
