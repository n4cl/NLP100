NLP100 with Python
===

言語処理100本ノックをPythonで実装  

言語処理100本ノック  
http://www.cl.ecei.tohoku.ac.jp/nlp100/  

## 動作環境
- macOS 10.11.6
- Python 2.7.13

## 実行結果
### 1章
[実行結果](/ch1/Chapter1.ipynb)

### 2章
[実行結果](/ch2/Chapter2.ipynb)

### 3章
[実行結果](/ch3/Chapter3.ipynb)

### 4章
[実行結果](/ch4/Chapter4.ipynb)

### 7章
[実行結果](/ch7/Chapter7.ipynb)

## 詳細
### 各chで利用するデータの準備
以下のスクリプトを実行する
> ./nlp100.sh

### 4章
- 要件
  - Middleware
    - MeCab 0.996
  - Python package
    - mecab-python 0.996
    - matplotlib 2.2.2
    - numpy 1.14.2

### 5章
- 要件
  - Middleware
    - CaboCha 0.69
    - graphviz 2.38.0
  - Python package
    - pydot 1.2.4
- ch5.py を実行後、ch5_40.py 以降が実行可能

### 7章
- 要件
  - Middleware
    - Redis 4.0.8
    - MongoDB 3.4
  - Python package
    - redis-py 2.10.6
    - pymongo 3.6.1
    - Flask 0.12.2
- ch7_60.py を実行すると、Redisにデータを登録
- ch7_64.py を実行すると、MongoDBにデータを登録
