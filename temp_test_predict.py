from models.predict_baseline import predict_news

text = "The government has announced a new policy to reduce inflation."
label, confidence = predict_news(text)

print("Prediction:", label)
print("Confidence:", confidence)
