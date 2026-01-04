from textblob import TextBlob

def analyze_sentiment(text):
    analysis = TextBlob(text)
    polarity = analysis.sentiment.polarity

    if polarity < -0.3:
        return "Negative", polarity
    elif polarity < 0.1:
        return "Neutral", polarity
    else:
        return "Positive", polarity

