from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.decomposition import TruncatedSVD
from wordcloud import WordCloud
import matplotlib.pyplot as plt

with open("converted.txt", "r", encoding="utf-8") as file:
    text = file.read()

tfidf_vectorizer = TfidfVectorizer(stop_words='english', max_features=100)
tfidf_matrix = tfidf_vectorizer.fit_transform([text])

lsa_model = TruncatedSVD(n_components=1, random_state=30)
lsa_topic_matrix = lsa_model.fit_transform(tfidf_matrix)

terms = tfidf_vectorizer.get_feature_names_out()
top_words_idx = lsa_model.components_[0].argsort()[::-1][:25] 
top_words = [terms[idx] for idx in top_words_idx]

excluded_words = ['pair', 'finance']
filtered_top_words = [word for word in top_words if word not in excluded_words]

wordcloud = WordCloud(width=800, height=400, background_color='white').generate(" ".join(filtered_top_words))
wordcloud.to_file("top_words_wordcloud.png")


plt.figure(figsize=(8, 4))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
