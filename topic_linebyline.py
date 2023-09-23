import nltk
import gensim
from nltk.tokenize import word_tokenize
from gensim import corpora, models
from collections import Counter
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
stop_words.update(['pair', 'finance', 'company'])

with open('converted.txt', 'r') as file:
    lines = file.readlines()

def preprocess_text(text):
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]
    return tokens

processed_lines = [preprocess_text(line) for line in lines]

dictionary = corpora.Dictionary(processed_lines)
corpus = [dictionary.doc2bow(processed_line) for processed_line in processed_lines]


lda_model = gensim.models.LdaModel(corpus, num_topics=20, id2word=dictionary)

topics = lda_model.print_topics(num_topics=20, num_words=5)
for topic_num, topic in topics:
    print(f"Topic {topic_num + 1}: {topic}")
