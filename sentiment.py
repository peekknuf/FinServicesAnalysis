import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer


sia = SentimentIntensityAnalyzer()

def analyze_sentiment(text):
    sentiment = sia.polarity_scores(text)
    return sentiment

with open('converted.txt', 'r') as file:
    lines = file.readlines()

line_sentiments = []
for line in lines:
    sentiment_scores = analyze_sentiment(line)
    line_sentiments.append(sentiment_scores)

# Output the results for each line
for i, sentiment_scores in enumerate(line_sentiments):
    print(f"Line {i + 1} Sentiment Analysis Results:")
    print(f"Line: {lines[i].strip()}")
    print(f"Compound Score: {sentiment_scores['compound']}")
    if sentiment_scores['compound'] >= 0.05:
        sentiment = "Positive"
    elif sentiment_scores['compound'] <= -0.05:
        sentiment = "Negative"
    else:
        sentiment = "Neutral"
    print(f"Sentiment: {sentiment}")
    print()

compound_scores = [sentiment_scores['compound'] for sentiment_scores in line_sentiments]
overall_sentiment = sum(compound_scores) / len(compound_scores)

print("Summary:")
print(f"Overall Compound Score: {overall_sentiment}")
if overall_sentiment >= 0.05:
    overall_sentiment_label = "Positive"
elif overall_sentiment <= -0.05:
    overall_sentiment_label = "Negative"
else:
    overall_sentiment_label = "Neutral"
print(f"Overall Sentiment: {overall_sentiment_label}")