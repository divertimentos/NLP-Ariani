import nltk
stopwords = nltk.corpus.stopwords.words('portuguese')
# stopwords = open("/Users/guiemi/github/ufscar/lab_6/nlp_ariani/movies_stopwords.txt")
filtered_corpus = list()

with open("corpus_completo.txt", "r") as file:
    raw_corpus = file.read()
    raw_corpus = raw_corpus.split()
    
    cleaned_corpus = list()
    blacklisted_words = set()
    
    for token in raw_corpus:
        if token in stopwords:
            blacklisted_words.add(token)
        
    print(blacklisted_words)

#     for token in tokenized_dirty_corpus:
#         if token not in stopwords:
#             filtered_corpus.append(token)
# with open("corpus_filtrado.txt", "w") as corpus_filtrado:
#     corpus_filtrado.write("".join(str((filtered_corpus))))
#     corpus_filtrado.write("\n".join(map(str, filtered_corpus)))
