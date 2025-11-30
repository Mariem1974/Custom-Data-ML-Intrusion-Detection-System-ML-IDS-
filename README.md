# 🛡 ML‑Based FTP Login Attack Detection (IDS Project)

This project implements an **Intrusion Detection System (IDS)** that detects suspicious FTP login activity using **Machine Learning**.  
All network traffic used to train the model was **self‑captured and labeled manually**, including both normal FTP sessions and password‑guessing attack attempts.

---

## 🔥 Project Goal
To build a machine‑learning detection model capable of distinguishing between **normal FTP traffic** and **unauthorized login attempts**, using a dataset we generated ourselves.

---

## 📌 Main Steps
1. Configured **Kali (attacker)** & **Metasploitable2 (victim)**
2. Captured **normal FTP traffic + login attack attempts**
3. Converted **PCAP files** to CSV dataset and added labels (**0 = normal, 1 = attack**)
4. Extracted features and selected the most relevant ones
5. Trained ML models to classify normal vs attack traffic
6. Evaluated **accuracy, precision, recall & F1‑score**

---

## 📊 Output & Results
- Final dataset included both **normal** and **attack** samples
- ML model learned to identify **malicious login attempts**
- Evaluation metrics were calculated to measure model performance  

> *(Add your exact numbers/results after training your model)*

---

## 🧠 Machine Learning Models Used
- **Random Forest**  
- **SVM**  
- *(Add others if used)*

---

## 📁 Files Included
| File | Description |
|---|---|
| `dataset.csv` | Self‑generated labeled dataset |
| `notebook.ipynb` | Model training, preprocessing & evaluation |
| `pcap/` | Raw captured network traffic |

---

### ⭐ Future Improvements
- Add more attack types  
- Increase dataset size  
- Try deep learning models
