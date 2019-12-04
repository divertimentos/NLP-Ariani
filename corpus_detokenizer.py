import re

with open("corpus_filtrado.txt") as corpus_filtrado:
    regex = re.compile('[^a-zA-Z]')
    regex = regex.sub('', str(corpus_filtrado[:10]))
print(regex)