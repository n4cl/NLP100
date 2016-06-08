# encoding: utf-8

"""
11. タブをスペースに置換
タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""


def replace_tab_to_space(file_path):
    with open(file_path, "r") as file:
        text = file.read()
        text = text.replace("\t", " ")
    
    return text

if __name__ == '__main__':
    print replace_tab_to_space("hightemp.txt")
