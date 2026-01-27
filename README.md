# AICTE_AIML_edunet foundation virtual internship
#### AICTE Batch 6 -AIML (2025-26)   ------------Project Title :-   Fake News Risk Analyzer 


# 📰 AI-Based Fake News Risk Analyzer

An AI-powered web application that analyzes **linguistic and semantic patterns** in news content to assess **potential misinformation risk**.  
The system demonstrates both **classical machine learning** and **transformer-based NLP approaches**, while clearly highlighting their strengths and limitations.

---

## 🚀 Project Overview

The rapid spread of misinformation through online platforms makes it difficult for users to distinguish between reliable and misleading content.  
This project aims to **analyze news text** and identify **language patterns commonly associated with misinformation**, rather than performing factual verification.

⚠️ **Important:**  
This system does **not fact-check claims** or verify real-world events.  
It performs **content-based linguistic analysis only**.

---

## 🧠 Models Used

### 🔹 1. Baseline ML Model (TF-IDF + SVM)
- Converts text into numerical features using **TF-IDF**
- Uses **Support Vector Machine (SVM)** for classification
- Focuses on **word frequency and writing style**

**Key Characteristics:**
- Fast and lightweight
- Works best with long-form articles
- Sensitive to dataset bias
- Does not understand semantic context
- Cannot verify factual correctness

---

### 🔹 2. Advanced NLP Model (DistilBERT)
- Transformer-based language model
- Captures **contextual and semantic relationships**
- Better handles short, neutral, and complex text

**Key Characteristics:**
- Improved contextual understanding
- Handles diverse writing styles
- Still does not perform fact-checking
- Large model size (not included in deployed version)

---
## 📊 Output

<div style="display: flex; gap: 10px;">
  <img alt="image" src="https://github.com/user-attachments/assets/20ab5faf-4ba7-46f2-8716-6b2258a95219" width="49.5%" />
  <img alt="image" src="https://github.com/user-attachments/assets/57a4f5e3-74b4-4a8e-861e-11c454916988" width="49.5%" />  
</div>

---
## ⚙️ Application Features

- Web-based interface built using **Streamlit**
- Model selection (Baseline / Advanced – local only)
- Clear disclaimer explaining system limitations
- Confidence / margin score for transparency
- Sidebar explanation of models and methodology

---

## 🖥️ Deployment Details

- **Platform:** Streamlit Cloud
- **Deployed Model:** Baseline ML (TF-IDF + SVM)
- **Advanced Model (DistilBERT):**  
  - Trained and evaluated locally
  - Excluded from GitHub and cloud deployment due to size constraints

📌 This deployment strategy follows standard machine learning practices for handling large models.

---

## 🧪 Example Use Cases

- Educational demonstration of fake news detection techniques
- Understanding limitations of content-based AI systems
- Comparing classical ML vs transformer-based NLP models
- Academic project and research presentation

---

## 🛠️ Tech Stack

- **Programming Language:** Python
- **Web Framework:** Streamlit
- **Machine Learning:** Scikit-learn
- **Deep Learning / NLP:** Hugging Face Transformers (DistilBERT)
- **Libraries:** Pandas, NumPy, Torch, Joblib

---

## 📂 Project Structure
```
FakeNewsDetector/
│
├── app.py
├── requirements.txt
├── models/
│   ├── svm_model.pkl
│   ├── tfidf.pkl
│   ├── bert_model/
│   │   ├── config.json
│   │   ├── model.safetensors
│   │   ├── tokenizer.json
│   │   ├── tokenizer_config.json
│   │   ├── special_tokens_map.json
│   │   └── vocab.txt
│   ├── predict_baseline.py
│   └── predict_bert.py
│
├── utils/
│   ├── preprocess.py
│   └── data_loader.py
│
└── requirements.txt

```


---

## ⚠️ Limitations

- Does not verify factual accuracy
- Does not cross-check sources
- May misclassify well-written misinformation
- Performance depends on training data style and domain

---

## 🔮 Future Enhancements

- Integration with fact-checking APIs (Snopes, PolitiFact)
- Source credibility scoring
- Knowledge-graph-based verification
- Multimodal fake news detection (text + image)
- Hosting large transformer models via external storage

---

## 🎓 Academic Note

This project intentionally highlights the **limitations of content-only fake news detection**, aligning with findings from current NLP research.  
It emphasizes **responsible AI design**, transparency, and ethical deployment.

---

## 📜 License

This project is intended for **educational and academic use** only.



