#!/bin/bash
set -eu

# ch4
curl -sS http://www.cl.ecei.tohoku.ac.jp/nlp100/data/neko.txt -o ./neko.txt
ln -sf ../neko.txt ./src/neko.txt
