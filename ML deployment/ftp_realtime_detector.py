import pyshark
import pandas as pd
import joblib
from datetime import datetime
import tkinter as tk
from tkinter import scrolledtext
from colorama import Fore, Style, init
import threading

# Initialize colorama
init(autoreset=True)

# -----------------------------
# Load model
# -----------------------------
model = joblib.load("ftp_ids_model.pkl")

# -----------------------------
# Logging
# -----------------------------
log_file = "ftp_alerts.log"

def log_alert(widget, src_ip, dst_ip, alert_type, confidence):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write to file
    with open(log_file, "a") as f:
        f.write(f"{timestamp} | {src_ip} -> {dst_ip} | {alert_type} | Confidence: {confidence:.2f}\n")

    # Write to correct GUI box
    widget.configure(state='normal')
    widget.insert(tk.END, f"{timestamp} | {src_ip} -> {dst_ip} | {alert_type} | Confidence: {confidence:.2f}\n")
    widget.yview(tk.END)
    widget.configure(state='disabled')

# -----------------------------
# Feature extraction
# -----------------------------
def extract_features(packet):
    try:
        data = {
            "frame.len": int(packet.length),
            "ip.len": int(packet.ip.len) if hasattr(packet, "ip") else 0,
            "ip.ttl": int(packet.ip.ttl) if hasattr(packet, "ip") else 0,
            "tcp.srcport": int(packet.tcp.srcport),
            "tcp.dstport": int(packet.tcp.dstport),
            "tcp.len": int(packet.tcp.len) if hasattr(packet.tcp, "len") else 0,
            "tcp.hdr_len": int(packet.tcp.hdr_len),
            "tcp.time_delta": float(packet.tcp.time_delta) if hasattr(packet.tcp, "time_delta") else 0.0,
            "tcp.flags": int(packet.tcp.flags, 16),
            "tcp.flags.syn": int(packet.tcp.flags_syn == 'TRUE'),
            "tcp.flags.ack": int(packet.tcp.flags_ack == 'TRUE'),
            "tcp.flags.fin": int(packet.tcp.flags_fin == 'TRUE'),
            "tcp.flags.reset": int(packet.tcp.flags_reset == 'TRUE'),
            "tcp.flags.push": int(packet.tcp.flags_push == 'TRUE'),
            "tcp.window_size_value": int(packet.tcp.window_size_value),
            "ftp.request.command": 1 if hasattr(packet, 'ftp') and hasattr(packet.ftp, 'request_command') else 0,
            "ftp.response.code": int(packet.ftp.response_code) if hasattr(packet, 'ftp') and hasattr(packet.ftp, 'response_code') else 0,
        }

        df = pd.DataFrame([data])
        df = df[model.feature_names_in_]
        return df
    except Exception:
        return None

# -----------------------------
# GUI Setup
# -----------------------------
root = tk.Tk()
root.title("FTP IDS Dashboard")
root.geometry("1000x600")

# --- Counters ---
attack_count = tk.IntVar(value=0)
normal_count = tk.IntVar(value=0)

tk.Label(root, text="Attack Count:", font=("Arial", 12)).pack()
tk.Label(root, textvariable=attack_count, fg="red", font=("Arial", 16)).pack()

tk.Label(root, text="Normal Count:", font=("Arial", 12)).pack()
tk.Label(root, textvariable=normal_count, fg="green", font=("Arial", 16)).pack()

# --- Frames for logs ---
frame_logs = tk.Frame(root)
frame_logs.pack(fill="both", expand=True)

frame_attack = tk.LabelFrame(frame_logs, text="🚨 ATTACK LOGS", fg="red", padx=5, pady=5)
frame_attack.pack(side="left", fill="both", expand=True)

frame_normal = tk.LabelFrame(frame_logs, text="✔ NORMAL LOGS", fg="green", padx=5, pady=5)
frame_normal.pack(side="right", fill="both", expand=True)

# --- Separate log windows ---
attack_log = scrolledtext.ScrolledText(frame_attack, width=60, height=25, state='disabled')
attack_log.pack(fill="both", expand=True)

normal_log = scrolledtext.ScrolledText(frame_normal, width=60, height=25, state='disabled')
normal_log.pack(fill="both", expand=True)

# -----------------------------
# Real-time capture
# -----------------------------
capture = pyshark.LiveCapture(interface="ens33", bpf_filter="tcp port 21")

def run_capture():
    for packet in capture:
        features = extract_features(packet)
        if features is None:
            continue

        probs = model.predict_proba(features)[0]
        pred = model.predict(features)[0]
        confidence = probs[1] if pred == 1 else probs[0]

        src_ip = packet.ip.src if hasattr(packet, "ip") else "N/A"
        dst_ip = packet.ip.dst if hasattr(packet, "ip") else "N/A"

        if pred == 1:
            attack_count.set(attack_count.get() + 1)
            print(Fore.RED + f"[ATTACK] {src_ip} -> {dst_ip} | Conf={confidence:.2f}")
            log_alert(attack_log, src_ip, dst_ip, "Attack", confidence)

        else:
            normal_count.set(normal_count.get() + 1)
            print(Fore.GREEN + f"[NORMAL] {src_ip} -> {dst_ip} | Conf={confidence:.2f}")
            log_alert(normal_log, src_ip, dst_ip, "Normal", confidence)

# Run sniffer in background
threading.Thread(target=run_capture, daemon=True).start()

root.mainloop()

