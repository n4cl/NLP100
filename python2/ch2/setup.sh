#!/bin/bash
set -eu

# ch2
curl -sS http://www.cl.ecei.tohoku.ac.jp/nlp100/data/hightemp.txt -o ./hightemp.txt
ln -sf ../hightemp.txt ./src/hightemp.txt
