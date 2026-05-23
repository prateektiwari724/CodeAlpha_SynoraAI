import json
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from chatbot.preprocess import clean_text


# Load FAQ data
with open("faq_data.json", "r") as file:
    faq_data = json.load(file)


# Extract questions
questions = [item["question"] for item in faq_data]


# Load AI model
model = SentenceTransformer("all-MiniLM-L6-v2")


# Create embeddings for FAQ questions
question_embeddings = model.encode(questions)


def get_response(user_input):

    # Clean user input
    cleaned_input = clean_text(user_input)

    # Convert user input into embedding
    user_embedding = model.encode([cleaned_input])

    # Calculate similarity
    similarity_scores = cosine_similarity(
        user_embedding,
        question_embeddings
    )

    # Find best matching question
    best_match_index = similarity_scores.argmax()

    # Get confidence score
    confidence_score = similarity_scores[0][best_match_index]

    # If confidence too low
    if confidence_score < 0.40:
        return {
            "answer": "Sorry, I couldn't understand your question.",
            "confidence": confidence_score
        }

    # Return best answer
    return {
        "answer": faq_data[best_match_index]["answer"],
        "confidence": confidence_score
    }