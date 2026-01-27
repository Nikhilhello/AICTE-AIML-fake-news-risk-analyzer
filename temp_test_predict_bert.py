from models.predict_bert import predict_news_bert

text = "The Reserve Bank of India has decided to keep the repo rate unchanged."
label, confidence = predict_news_bert(text)

print("Prediction:", label)
print("Confidence:", confidence)
