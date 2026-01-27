# import sys
# import os
# import joblib

# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# from utils.preprocess import clean_text

# # Load saved model & vectorizer
# model = joblib.load("models/svm_model.pkl")
# tfidf = joblib.load("models/tfidf.pkl")

# def predict_news(text):
#     cleaned_text = clean_text(text)
#     vectorized_text = tfidf.transform([cleaned_text])

#     prediction = model.predict(vectorized_text)[0]
#     confidence = model.decision_function(vectorized_text)[0]

#     label = "FAKE" if prediction == 1 else "REAL"
#     confidence = round(abs(confidence), 3)

#     return label, confidence



import sys
import os
import joblib

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from utils.preprocess import clean_text

# Load baseline model
model = joblib.load("models/svm_model.pkl")
tfidf = joblib.load("models/tfidf.pkl")

def predict_news(text):
    cleaned = clean_text(text)
    vectorized = tfidf.transform([cleaned])

    pred = model.predict(vectorized)[0]
    score = model.decision_function(vectorized)[0]

    # IMPORTANT: baseline is stylistic, not factual
    if abs(score) < 0.5:
        return "NEEDS FACT CHECKING", round(abs(score), 3)

    label = "LIKELY REAL (Style-Based)" if pred == 0 else "HIGH MISINFORMATION RISK"
    return label, round(abs(score), 3)
