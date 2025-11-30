🛡 ML‑Based FTP Login Attack Detection (IDS Project)

This project implements an Intrusion Detection System (IDS) that detects suspicious FTP login activity using Machine Learning.
All network traffic used to train the model was self‑captured and labeled manually, including both normal FTP sessions and password‑guessing attack attempts.

🔥 Project Goal

To build a machine‑learning detection model capable of distinguishing between normal FTP traffic and unauthorized login attempts, using a dataset we generated ourselves.

📌 Main Steps

Configured Kali (attacker) & Metasploitable2 (victim)

Captured normal FTP traffic + login attack attempts

Converted PCAP files to CSV dataset and added labels (0 = normal, 1 = attack)

Extracted features and selected the most relevant ones

Trained ML models to classify normal vs attack traffic

Evaluated accuracy, precision, recall & F1‑score

📊 Output & Results

Final dataset included both normal and attack samples

ML model learned to identify malicious login attempts

Evaluation metrics were calculated to measure model performance
