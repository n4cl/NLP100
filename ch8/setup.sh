#!/bin/bash
set -eu

curl -sS http://www.cs.cornell.edu/people/pabo/movie-review-data/rt-polaritydata.tar.gz -o ./src/rt-polaritydata.tar.gz
tar -zxf ./src/rt-polaritydata.tar.gz -C ./src/
nkf -w --overwrite ./src/rt-polaritydata/rt-polarity.pos
nkf -w --overwrite ./src/rt-polaritydata/rt-polarity.neg
