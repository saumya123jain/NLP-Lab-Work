import nltk

# Sample corpus
text_file = open('corpus.txt', 'r')
corpus = text_file.read()

# Tokenize the corpus into individual words
tokens = nltk.word_tokenize(corpus)

print(tokens[:10])