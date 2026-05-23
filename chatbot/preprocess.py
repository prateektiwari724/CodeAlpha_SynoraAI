import re
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords


# Load English stopwords
stop_words = set(stopwords.words("english"))


def clean_text(text):

    # Convert text to lowercase
    text = text.lower()

    # Remove special characters
    text = re.sub(r"[^a-zA-Z0-9\s]", "", text)

    # Tokenize text
    tokens = word_tokenize(text)

    # Remove stopwords
    filtered_tokens = [
        word for word in tokens
        if word not in stop_words
    ]

    # Join words back
    cleaned_text = " ".join(filtered_tokens)

    return cleaned_text