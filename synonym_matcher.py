text_file = open('corpus_completo.txt', 'r+')
# token_list = list()
# for token in text_file:
#     token_list.append(token)
#     print(token_list.count(token))

# print(token_list)
# text_file.close()
for token in text_file:
    if token == "isto é":
        print(token)