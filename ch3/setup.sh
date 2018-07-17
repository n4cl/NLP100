#!/bin/bash
set -eu

# ch3
curl -sS http://www.cl.ecei.tohoku.ac.jp/nlp100/data/jawiki-country.json.gz -o ./jawiki-country.json.gz
gunzip -c ./jawiki-country.json.gz > ./jawiki-country.json
ln -sf ../jawiki-country.json ./src/jawiki-country.json
