# import sys
# import os
# import torch
# from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

# # Fix path so utils/models can be found
# sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# # Load tokenizer and model
# MODEL_PATH = "models/bert_model"

# tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)
# model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)

# model.eval()  # evaluation mode

# # def predict_news_bert(text):
# #     inputs = tokenizer(
# #         text,
# #         truncation=True,
# #         padding=True,
# #         max_length=256,
# #         return_tensors="pt"
# #     )

# #     with torch.no_grad():
# #         outputs = model(**inputs)

# #     logits = outputs.logits
# #     probs = torch.softmax(logits, dim=1)

# #     pred = torch.argmax(probs, dim=1).item()
# #     confidence = probs[0][pred].item()

# #     # label = "FAKE" if pred == 1 else "REAL"
# #     label = "REAL" if pred == 1 else "FAKE"



# #     return label, round(confidence, 3)


# #--------------------------------------------------------------no change-----------------------
# # def predict_news_bert(text):
# #     inputs = tokenizer(
# #         text,
# #         truncation=True,
# #         padding=True,
# #         max_length=256,
# #         return_tensors="pt"
# #     )

# #     with torch.no_grad():
# #         outputs = model(**inputs)

# #     probs = torch.softmax(outputs.logits, dim=1)
# #     confidence, pred = torch.max(probs, dim=1)

# #     confidence = confidence.item()
# #     pred = pred.item()

# #     # Confidence-based decision
# #     if confidence >= 0.75:
# #         label = "REAL" if pred == 1 else "FAKE"
# #     else:
# #         label = "POSSIBLY MISLEADING"

# #     return label, round(confidence, 3)




# def predict_news_bert(text):
#     inputs = tokenizer(
#         text,
#         truncation=True,
#         padding=True,
#         max_length=256,
#         return_tensors="pt"
#     )

#     with torch.no_grad():
#         outputs = model(**inputs)

#     logits = outputs.logits.squeeze()  # shape: [2]

#     # logits[0] -> class 0
#     # logits[1] -> class 1
#     logit_diff = torch.abs(logits[1] - logits[0]).item()

#     pred = torch.argmax(logits).item()

#     # FINAL, SAFE DECISION LOGIC
#     if logit_diff < 1.0:
#         label = "POSSIBLY MISLEADING"
#         confidence = logit_diff
#     else:
#         label = "REAL" if pred == 1 else "FAKE"
#         confidence = logit_diff

#     return label, round(confidence, 3)




import sys
import os
import torch
from transformers import DistilBertTokenizerFast, DistilBertForSequenceClassification

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

MODEL_PATH = "models/bert_model"

tokenizer = DistilBertTokenizerFast.from_pretrained(MODEL_PATH)
model = DistilBertForSequenceClassification.from_pretrained(MODEL_PATH)
model.eval()

def predict_news_bert(text):
    inputs = tokenizer(
        text,
        truncation=True,
        padding=True,
        max_length=256,
        return_tensors="pt"
    )

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits.squeeze()
    diff = torch.abs(logits[1] - logits[0]).item()

    # We do NOT claim factual truth
    if diff < 1.0:
        return "NEEDS FACT CHECKING", round(diff, 3)

    pred = torch.argmax(logits).item()

    if pred == 1:
        return "NO LINGUISTIC INDICATORS OF FAKE NEWS", round(diff, 3)
    else:
        return "HIGH MISINFORMATION RISK", round(diff, 3)
