# 🛡 ML-Based FTP Login Attack Detection (IDS Project)

This project implements a Machine Learning–based Intrusion Detection System (IDS) designed to detect suspicious FTP login activity.  
All traffic used to train the model was **self-captured and manually labeled**, including both normal sessions and brute-force login attempts.

---

## 🔥 Project Goal

Build a machine-learning model that accurately classifies FTP traffic as **normal** or **attack**, using real network traffic generated in a controlled lab environment.

---

## 📌 Main Steps

- Setup of **Kali (attacker)** and **Metasploitable2 (victim)**
- Capturing normal FTP activity + brute-force login attempts
- Converting **PCAP files to CSV**
- Manual labeling (`0 = normal`, `1 = attack`)
- Feature extraction + preprocessing
- Training and evaluating the ML model

---

## 🧠 Machine Learning Model

We used a **Random Forest Classifier**.

### Why Random Forest?

- Very high accuracy on tabular network data  
- Robust against noise  
- Handles non-linear relationships  
- Reduces overfitting compared to single decision trees  
- Provides feature importance for analysis  

---

## 📊 Model Performance

The Random Forest model achieved strong performance on the labeled dataset.

### ✔ Final Accuracy: **98.71%**

### ✔ Classification Report

| Class   | Precision | Recall | F1-Score |
|---------|-----------|--------|----------|
| Normal  | 0.99      | 0.99   | 0.99     |
| Attack  | 0.97      | 0.99   | 0.98     |

### ✔ Confusion Matrix

*(Replace `IMAGE_LINK_HERE` with the direct link to your confusion matrix image after uploading it to GitHub.)*

`![Confusion Matrix](https://raw.githubusercontent.com/Mariem1974/Custom-Data-ML-Intrusion-Detection-System-ML-IDS-/main/confusion_matrix.jpeg
)`

---

## 📁 Project Structure

| File / Folder | Description |
|---------------|-------------|
| `dataset/pcap/` | Raw PCAP files captured during experiments |
| `dataset/raw/` | CSV files generated from PCAP before preprocessing |
| `dataset/cleaned/` | Final cleaned + merged dataset (`merged_cleaned.csv`) |
| `notebooks/feature_extraction.ipynb` | PCAP → CSV conversion + feature extraction |
| `notebooks/model_training.ipynb` | Preprocessing + Random Forest training |
| `README.md` | Project documentation |

---

## ⭐ Future Enhancements

- Add more attack types (SSH brute force, DoS, SMB enumeration)  
- Expand dataset size for higher generalization  
- Try advanced ML models: **XGBoost**, **SVM**, **LightGBM**  
- Real-time IDS deployment with live packet sniffing  
- Visualization dashboard integration  

