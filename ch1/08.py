# encoding: utf-8

"""
08. 暗号文
与えられた文字列の各文字を，以下の仕様で変換する関数cipherを実装せよ．

英小文字ならば(219 - 文字コード)の文字に置換
その他の文字はそのまま出力
この関数を用い，英語のメッセージを暗号化・復号化せよ．
"""


def cipher(message):
    encryption = ""
    for character in message:
        if character.islower():
            encryption += str(219 - ord(character))
        else:
            encryption += character

    return encryption

if __name__ == '__main__':
    text = "test message."
    print cipher(text)
