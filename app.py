# import streamlit as st
# from models.predict_baseline import predict_news

# st.set_page_config(page_title="Fake News Detector", layout="centered")

# st.title("📰 Fake News Detector")
# st.write("Detect whether a news article is **Fake** or **Real** using AI.")

# news_text = st.text_area(
#     "Paste the news article text below:",
#     height=250
# )

# if st.button("Analyze News"):
#     if news_text.strip() == "":
#         st.warning("Please enter some news text.")
#     else:
#         with st.spinner("Analyzing..."):
#             label, confidence = predict_news(news_text)

#         if label == "FAKE":
#             st.error(f"🛑 Prediction: {label}")
#         else:
#             st.success(f"✅ Prediction: {label}")

#         st.write(f"**Confidence Score:** {confidence}")



# =======================================================================================================

# import streamlit as st
# from models.predict_baseline import predict_news

# # Page config
# st.set_page_config(
#     page_title="Fake News Detector",
#     layout="centered"
# )

# # Title
# st.title("📰 Fake News Detector for Students")

# st.write(
#     """
# This application uses **Machine Learning** to classify news articles as **Fake** or **Real**.

# ⚠️ **Important Note:**  
# - The current baseline model works best with **full news articles or paragraphs**.  
# - Short headlines or very neutral content may be misclassified.  
# - An advanced **BERT-based model** will be added to improve accuracy.
# """
# )

# # Input area
# news_text = st.text_area(
#     "Paste the full news article below (recommended: 3–5 paragraphs):",
#     height=280
# )

# # Analyze button
# if st.button("Analyze News"):
#     if news_text.strip() == "":
#         st.warning("Please enter some news text before clicking Analyze.")
#     elif len(news_text.split()) < 30:
#         st.warning(
#             "The text seems too short. "
#             "For better accuracy, please paste a full news article or paragraph."
#         )
#     else:
#         with st.spinner("Analyzing the news article..."):
#             label, confidence = predict_news(news_text)

#         st.subheader("🔍 Analysis Result")

#         if label == "FAKE":
#             st.error("🛑 Prediction: FAKE NEWS")
#         else:
#             st.success("✅ Prediction: REAL NEWS")

#         st.write(f"**Model Confidence Score:** {confidence}")

#         st.info(
#             "This prediction is based on textual patterns learned from historical news data. "
#             "It does not verify facts using external sources."
#         )

# # Footer
# st.markdown("---")
# st.caption(
#     "📌 Project: AI-Based Fake News Detector | "
#     "Baseline Model: TF-IDF + SVM | "
#     "Next Upgrade: DistilBERT (Transformer)"
# )

#-===========================---------=--===============-=---==-=-=-=-=-=-=-=-=-=-==--=-=-=-=-=-=-==-

# import streamlit as st
# from models.predict_baseline import predict_news
# from models.predict_bert import predict_news_bert

# st.set_page_config(page_title="Fake News Detector", layout="centered")

# st.title("📰 Fake News Detector for Students")

# st.write(
#     """
# This application uses **Machine Learning and Deep Learning** to classify news articles
# as **Fake** or **Real**.

# ⚠️ **Important Notes**
# - Baseline model (TF-IDF + SVM) works best for long articles
# - BERT model handles short and neutral news much better
# """
# )

# # Model selector
# model_choice = st.radio(
#     "Select Model:",
#     ("Baseline (TF-IDF + SVM)", "Advanced (DistilBERT)")
# )

# news_text = st.text_area(
#     "Paste the news article or paragraph below:",
#     height=280
# )

# if st.button("Analyze News"):
#     if news_text.strip() == "":
#         st.warning("Please enter some news text.")
#     else:
#         with st.spinner("Analyzing..."):
#             if model_choice == "Baseline (TF-IDF + SVM)":
#                 label, confidence = predict_news(news_text)
#                 st.caption("Model Used: TF-IDF + SVM (Baseline)")
#             else:
#                 label, confidence = predict_news_bert(news_text)
#                 st.caption("Model Used: DistilBERT (Advanced)")

#         st.subheader("🔍 Result")

#         # if label == "FAKE":
#         #     st.error("🛑 Prediction: FAKE NEWS")
#         # else:
#         #     st.success("✅ Prediction: REAL NEWS")

#         if label == "FAKE":
#             st.error("🛑 Prediction: FAKE NEWS")
#         elif label == "REAL":
#             st.success("✅ Prediction: REAL NEWS")
#         else:
#             st.warning("⚠️ Prediction: POSSIBLY MISLEADING / NEEDS VERIFICATION")


#         st.write(f"**Confidence Score:** {confidence}")

# st.markdown("---")
# st.caption(
#     "AI-Based Fake News Detector | "
#     "Baseline: TF-IDF + SVM | "
#     "Advanced: DistilBERT"
# )




# ==================max fix==============
# import streamlit as st
# from models.predict_baseline import predict_news
# from models.predict_bert import predict_news_bert

# st.set_page_config(page_title="Fake News Risk Analyzer", layout="centered")

# st.title("📰 AI-Based Fake News Risk Analyzer")

# st.write(
#     """
# This application analyzes **linguistic and semantic patterns** in news content to
# identify **potential misinformation risk**.

# ⚠️ **Important Disclaimer**
# - This system does **NOT verify factual correctness**
# - It does **NOT check sources or real-world events**
# - It identifies **language patterns commonly associated with misinformation**
# """
# )

# model_choice = st.radio(
#     "Select Analysis Model:",
#     ("Baseline ML (TF-IDF + SVM)", "Advanced NLP (DistilBERT)")
# )

# news_text = st.text_area(
#     "Paste the news article or paragraph below:",
#     height=300
# )

# if st.button("Analyze Content"):
#     if news_text.strip() == "":
#         st.warning("Please enter news text for analysis.")
#     else:
#         with st.spinner("Analyzing linguistic patterns..."):
#             if model_choice == "Baseline ML (TF-IDF + SVM)":
#                 label, confidence = predict_news(news_text)
#                 st.caption("Model Used: TF-IDF + SVM (Style-based analysis)")
#             else:
#                 label, confidence = predict_news_bert(news_text)
#                 st.caption("Model Used: DistilBERT (Contextual language analysis)")

#         st.subheader("🔍 Analysis Result")

#         if "HIGH MISINFORMATION" in label:
#             st.error(f"🛑 Result: {label}")
#         elif "NO LINGUISTIC" in label or "LIKELY REAL" in label:
#             st.success(f"✅ Result: {label}")
#         else:
#             st.warning(f"⚠️ Result: {label}")

#         st.write(f"**Model Confidence / Margin Score:** {confidence}")

#         st.info(
#             "ℹ️ This result indicates linguistic risk level only. "
#             "Fact-checking with trusted sources is recommended."
#         )

# st.markdown("---")
# st.caption(
#     "Final Year Project | AI-Based Fake News Risk Analysis | "
#     "Baseline ML + Transformer NLP"
# )

import streamlit as st
from models.predict_baseline import predict_news
from models.predict_bert import predict_news_bert

# Page configuration
st.set_page_config(page_title="Fake News Risk Analyzer", layout="centered")

# ---------------- SIDEBAR ----------------
st.sidebar.title("🧠 Analysis Models")

st.sidebar.markdown(
    """
### 🔹 Baseline ML (TF-IDF + SVM)

**How it works:**
- Converts text into numerical features using **TF-IDF**
- Learns patterns using a **Support Vector Machine**
- Focuses on **word frequency and writing style**

**Important Points:**
- Fast and lightweight
- Works best with **long news articles**
- Sensitive to dataset bias
- Does **not understand meaning or context**
- May misclassify neutral or short news

---

### 🔹 Advanced NLP (DistilBERT)

**How it works:**
- Uses a **Transformer-based language model**
- Understands **context and sentence structure**
- Analyzes relationships between words
- Fine-tuned on fake vs real news data

**Important Points:**
- Handles **short, neutral, and complex text** better
- Captures semantic meaning
- Still **does not verify factual correctness**
- Cannot replace human fact-checking
"""
)

st.sidebar.markdown("---")
st.sidebar.caption("ℹ️ Models analyze language patterns, not truth.")

# ---------------- MAIN PAGE ----------------
st.title("📰 AI-Based Fake News Risk Analyzer")

st.write(
    """
This application analyzes **linguistic and semantic patterns** in news content to
assess **potential misinformation risk**.

⚠️ **Disclaimer**
- The system does **NOT verify facts**
- It does **NOT check sources or real-world events**
- Results indicate **language-based risk only**
"""
)

# Model selector
model_choice = st.radio(
    "Select Analysis Model:",
    ("Baseline ML (TF-IDF + SVM)", "Advanced NLP (DistilBERT)")
)

# Input area
news_text = st.text_area(
    "Paste the news article or paragraph below:",
    height=300
)

# Analyze button
if st.button("Analyze Content"):
    if news_text.strip() == "":
        st.warning("Please enter news text for analysis.")
    else:
        with st.spinner("Analyzing linguistic patterns..."):
            if model_choice == "Baseline ML (TF-IDF + SVM)":
                label, confidence = predict_news(news_text)
                st.caption("Model Used: TF-IDF + SVM (Style-based analysis)")
            else:
                label, confidence = predict_news_bert(news_text)
                st.caption("Model Used: DistilBERT (Contextual language analysis)")

        st.subheader("🔍 Analysis Result")

        if "HIGH MISINFORMATION" in label:
            st.error(f"🛑 Result: {label}")
        elif "NO LINGUISTIC" in label or "LIKELY REAL" in label:
            st.success(f"✅ Result: {label}")
        else:
            st.warning(f"⚠️ Result: {label}")

        st.write(f"**Model Confidence / Margin Score:** {confidence}")

        st.info(
            "ℹ️ This output reflects linguistic risk assessment only. "
            "Users are encouraged to verify information using trusted fact-checking sources."
        )

# Footer
st.markdown("---")
st.caption(
    "Nikhil K | AI-Based Fake News Risk Analyzer | "
    "Baseline ML + Transformer NLP"
)
