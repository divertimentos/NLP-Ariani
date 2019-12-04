import nltk
# stopwords = nltk.corpus.stopwords.words('portuguese')
stopwords = open("/Users/guiemi/github/ufscar/lab_6/nlp_ariani/movies_stopwords.txt")
filtered_corpus = list()

with open("corpus_completo.txt") as file:
    dirty_corpus = file.read()
    tokenized_dirty_corpus = dirty_corpus.split( )
    for token in tokenized_dirty_corpus:
        if token not in stopwords:
            filtered_corpus.append(token)
with open("corpus_filtrado.txt", "w") as corpus_filtrado:
    corpus_filtrado.write("".join(str((filtered_corpus))))
    corpus_filtrado.write("\n".join(map(str, filtered_corpus)))
