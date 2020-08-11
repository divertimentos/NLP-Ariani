#!/bin/sh

grep -o -E "[[:alnum:]]+ como [[:alnum:]]+| [[:alnum:]]+ (tal como|tais como)|\w*, sobretudo \w*" corpus_completo.txt  /Users/guiemi/github/ufscar/lab_6/nlp_ariani/movies_stopwords.txt  matches.txt