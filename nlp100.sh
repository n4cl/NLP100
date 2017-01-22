#!/bin/bash
set -eu

# ch2
curl -sS http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt -o ./ch2/hightemp.txt

# ch3
curl -sS http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz -o ./ch3/jawiki-country.json.gz
gunzip -c ./ch3/jawiki-country.json.gz > ./ch3/jawiki-country.json

# ch4
curl -sS http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt -o ./ch4/neko.txt

# ch5
cp -a ./ch4/neko.txt ./ch5/neko.txt
