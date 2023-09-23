import nltk
import gensim
from nltk.tokenize import word_tokenize
from gensim import corpora, models
from collections import Counter
from nltk.corpus import stopwords

stop_words = set(stopwords.words('english'))
stop_words.update(['pair', 'finance', 'company'])

with open('converted.txt', 'r') as file:
    text = file.read()  # Read the entire text

def preprocess_text(text):
    # Tokenize and remove stopwords
    tokens = word_tokenize(text)
    tokens = [word.lower() for word in tokens if word.isalpha() and word.lower() not in stop_words]
    return tokens

processed_text = preprocess_text(text)

dictionary = corpora.Dictionary([processed_text])
corpus = [dictionary.doc2bow(processed_text)]

lda_model = gensim.models.LdaModel(corpus, num_topics=3, id2word=dictionary)

topics = lda_model.print_topics(num_topics=3, num_words=10)
for topic_num, topic in topics:
    print(f"Topic {topic_num + 1}: {topic}")
