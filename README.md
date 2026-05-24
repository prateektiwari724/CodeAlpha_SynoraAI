# Synora AI – Intelligent E-Commerce FAQ Chatbot

<div align="center">

![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red?style=for-the-badge&logo=streamlit)
![NLP](https://img.shields.io/badge/NLP-NLTK-green?style=for-the-badge)
![Machine Learning](https://img.shields.io/badge/ML-Scikit--Learn-orange?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Deployed-success?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-purple?style=for-the-badge)

</div>

---

# Project Overview

Synora AI is an AI-powered FAQ chatbot developed for e-commerce customer support. The chatbot uses Natural Language Processing (NLP) and Machine Learning techniques to understand user queries and return the most relevant FAQ responses.

The system preprocesses textual queries using NLP, converts them into TF-IDF vectors, and applies cosine similarity to identify the best matching answer from the FAQ dataset.

The chatbot is deployed using Streamlit Cloud and provides an interactive real-time chat interface.

---

# Live Deployment

## Live Demo

```text
https://YOUR-STREAMLIT-APP-LINK.streamlit.app
```

### Important Note

This project is deployed on the free tier of Streamlit Cloud.

If the app remains inactive for approximately 13–15 minutes, Streamlit automatically puts the application to sleep to save resources.

When opening the app again, you may see a:

```text
Yes, get this app back up!
```

button.

Simply click that button and wait a few seconds for the app to restart.

---

# Features

- AI-powered FAQ chatbot
- NLP preprocessing using NLTK
- TF-IDF vectorization
- Cosine similarity-based matching
- Real-time chatbot UI
- E-commerce customer support use cases
- Interactive dark-themed interface
- Cloud deployment using Streamlit

---

# Complete Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Frontend | Streamlit, HTML, CSS |
| Backend | Python |
| NLP Processing | NLTK |
| Machine Learning | Scikit-learn |
| Vectorization | TF-IDF Vectorizer |
| Similarity Matching | Cosine Similarity |
| Data Storage | JSON |
| Numerical Computing | NumPy |
| Data Handling | Pandas |
| Version Control | Git, GitHub |
| Deployment | Streamlit Community Cloud |
| Runtime Environment | Python 3.10 |
| Development Environment | VS Code |

---

# System Architecture

```text
User
   ↓
Streamlit Chat UI
   ↓
app.py
   ↓
NLP Preprocessing
   ↓
TF-IDF Vectorization
   ↓
Cosine Similarity Matching
   ↓
Best FAQ Selection
   ↓
Retrieve Answer from FAQ Dataset
   ↓
Display Response to User
```

---

# High-Level Pipeline

```text
1. User enters query
2. Query preprocessing using NLP
3. Text converted into TF-IDF vectors
4. Cosine similarity calculation
5. Best matching FAQ identified
6. Corresponding answer retrieved
7. Response displayed in chatbot UI
```

---

# Project Structure

```text
SYNORA-AI/
│
├── chatbot/
│   ├── chatbot_engine.py
│   └── preprocess.py
│
├── app.py
├── faq_data.json
├── requirements.txt
├── .gitignore
└── README.md
```

---

# NLP Techniques Used

The chatbot uses the following NLP preprocessing techniques:

- Lowercasing
- Tokenization
- Stopword Removal
- Text Cleaning
- Text Normalization

These preprocessing steps improve similarity matching accuracy and response quality.

---

# Machine Learning Workflow

## TF-IDF Vectorization

The FAQ text data is converted into numerical vectors using TF-IDF (Term Frequency – Inverse Document Frequency).

---

## Cosine Similarity

The chatbot compares:

- User query vector
- FAQ question vectors

The FAQ with the highest similarity score is selected as the best matching answer.

---

# Dataset

The project uses a custom FAQ dataset stored in:

```text
faq_data.json
```

The dataset contains:
- Customer support questions
- Corresponding answers

Examples:
- Refund policy
- Order tracking
- Shipping information
- Payment issues
- Account support

---

# Sample Use Cases

## E-Commerce Customer Support

Users can ask:
- “How can I track my order?”
- “How do refunds work?”
- “Can I cancel my order?”
- “What payment methods are accepted?”

---

## Shipping & Delivery Assistance

The chatbot can answer:
- Shipping timelines
- Delivery-related queries
- Order tracking support

---

## Payment & Refund Queries

The chatbot assists users with:
- Payment status
- Refund process
- Failed transaction support

---

## Account & Login Support

Users can get help with:
- Password reset
- Login issues
- Account-related FAQs

---

# User Interface

The chatbot interface includes:

- Interactive chat UI
- Real-time response generation
- Sidebar support section
- Modern dark theme
- Responsive layout

---

# Future Improvements

- LLM Integration
- Semantic Search using Sentence Transformers
- Retrieval-Augmented Generation (RAG)
- Vector Database Integration (FAISS / ChromaDB)
- Conversation Memory
- Voice Assistant Integration
- Multi-language Support
- Real-Time Order Tracking APIs
- User Authentication System
- Admin Analytics Dashboard
- Sentiment Analysis for Customer Queries

---

# Key Learnings

Through this project, the following concepts were implemented and learned:

- NLP preprocessing
- TF-IDF vectorization
- cosine similarity
- chatbot architecture
- Streamlit deployment
- dependency management
- GitHub version control
- cloud deployment debugging

---

# License

This project is licensed under the MIT License.

---

# Author

## Prateek Tiwari

AI/ML Enthusiast | NLP Developer | Python Developer

---

<div align="center">

If you like this project, consider giving it a star on GitHub.

</div>
