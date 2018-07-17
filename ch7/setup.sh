#!/bin/bash
set -eu

# ch7
curl -sS http://www.cl.ecei.tohoku.ac.jp/nlp100/data/artist.json.gz -o ./ch7/src/artist.json.gz
gunzip -c ./ch7/src/artist.json.gz > ./ch7/src/artist.json