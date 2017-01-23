NLP100 with Python
===

言語処理100本ノックをPythonで実装  

言語処理100本ノック  
http://www.cl.ecei.tohoku.ac.jp/nlp100/  
利用データは、次のURL内から取得する  
http://www.cl.ecei.tohoku.ac.jp/nlp100/#data

## 動作環境
- macOS 10.11.6
- Python 2.7.9

## 詳細
### 各chで利用するデータの準備
以下のスクリプトを実行する
> ./nlp100.sh

### ch3の注意事項
- 20.py を実行後、21.py 以降が実行可能

### ch4の注意事項
- 要件
  - MeCab 0.996
  - mecab-python 0.996
  - matplotlib 1.5.3
  - numpy 1.11.3

### ch5の注意事項
- 要件
  - CaboCha 0.69
- ch5.py を実行後、ch5_40.py 以降が実行可能