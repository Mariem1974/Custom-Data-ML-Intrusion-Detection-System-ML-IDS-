# 🛡 ML‑Based FTP Login Attack Detection (IDS Project)

This project implements an **Intrusion Detection System (IDS)** that detects suspicious FTP login activity using **Machine Learning (ML)**.  
All network traffic used to train the model was **self‑captured and labeled manually**, including both normal FTP sessions and unauthorized login attempts.

---

## 🔥 Project Goal
To build a machine‑learning detection model that classifies network activity as **normal** or **FTP attack**, using a dataset created from real traffic generated in our own lab environment.

---

## 📌 Main Steps
1. Set up **Kali (attacker)** and **Metasploitable2 (victim)**
2. Captured **normal FTP traffic + login attack attempts**
3. Converted PCAP files to CSV and labeled data (**0 = normal, 1 = attack**)
4. Extracted and selected the most useful features for training
5. Trained a Machine Learning model to identify suspicious login behavior
6. Evaluated model performance using standard classification metrics

---

## 🧠 Machine Learning Model Used
We used **Logistic Regression** as the main classification model.

### Why Logistic Regression?
- Lightweight and fast  
- Works well with binary classification (normal vs attack)  
- Easy to interpret and visualize  
- Suitable for early‑stage IDS detection research  

---

## 📊 Output & Results
- Dataset contained **normal login events + attack attempts**
- Logistic Regression successfully learned to detect abnormal activity
- Evaluation metrics were calculated to measure performance:

📌 *Add your values later:*  
``Accuracy – Precision – Recall – F1 score``  
*(Replace here with your actual numbers after training)*

---

## 📁 Project Files
| File | Description |
|---|---|
| `dataset.csv` | Final labeled dataset |
| `notebook.ipynb` | Preprocessing + Logistic Regression training + evaluation |
| `pcap/` | Raw PCAP traffic used for dataset generation |

---

### ⭐ Future Improvements
- Add more attack scenarios (SSH, DoS, SMB, etc.)
- Expand dataset size for better generalization
- Experiment with other ML models like Random Forest / SVM / Neural Networks
