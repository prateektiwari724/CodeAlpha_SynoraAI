import json
import nltk

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download required NLTK data
try:
    nltk.data.find("tokenizers/punkt")
except LookupError:
    nltk.download("punkt")

try:
    nltk.data.find("corpora/stopwords")
except LookupError:
    nltk.download("stopwords")

# Load FAQ data
with open("faq_data.json", "r", encoding="utf-8") as file:
    faq_data = json.load(file)

questions = [item["question"] for item in faq_data]
answers = [item["answer"] for item in faq_data]

# Stopwords
stop_words = set(stopwords.words("english"))

# Text preprocessing
def preprocess(text):

    words = word_tokenize(text.lower())

    filtered_words = [
        word for word in words
        if word.isalnum() and word not in stop_words
    ]

    return " ".join(filtered_words)

# Process all FAQ questions
processed_questions = [preprocess(q) for q in questions]

# Better TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    sublinear_tf=True
)

question_vectors = vectorizer.fit_transform(processed_questions)

# Chatbot response function
def get_response(user_input):

    processed_input = preprocess(user_input)

    user_vector = vectorizer.transform([processed_input])

    similarity_scores = cosine_similarity(
        user_vector,
        question_vectors
    )

    best_match_index = similarity_scores.argmax()

    best_score = similarity_scores[0][best_match_index]

    # Better confidence threshold
    if best_score >= 0.35:
        return answers[best_match_index]

    return "Sorry, I could not understand your question clearly."