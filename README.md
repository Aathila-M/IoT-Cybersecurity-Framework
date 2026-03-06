# IoT Cybersecurity Framework for Smart City Networks

This project presents a **Machine Learning-Driven Cybersecurity Framework** designed for **IoT and Smart City Wireless Networks**.  
The system detects malicious network traffic, performs penetration testing, and visualizes security alerts through a **Security Operations Center (SOC) Dashboard**.

---

## Features

- Machine Learning Intrusion Detection System (Random Forest)
- SOC Cybersecurity Dashboard (Python + Tkinter)
- Port Scanner for Vulnerability Detection
- IoT Device Discovery in Local Network
- Network Traffic Visualization
- Automatic Attack Alerts
- Confusion Matrix Evaluation

---

## Technologies Used

- Python
- Scikit-learn
- Pandas
- Matplotlib
- Seaborn
- Tkinter
- Socket Programming

---

## System Architecture

IoT Devices  
↓  
Network Packet Monitoring  
↓  
Feature Extraction  
↓  
Machine Learning IDS  
(Random Forest)  
↓  
SOC Dashboard  

Modules:
- Attack Detection
- Port Scanner
- Network Traffic Graph
- IoT Device Discovery

---

## Project Screenshots

### SOC Dashboard
(<screenshots/dashboard.png>)

### device
(<screenshots/device.png>)

### Attack Detection
(<screenshots/detect attack.png>)
(<screenshots/detect attack(cyber attack).png>)

### confusion matrix
(<screenshots/confusion matrix.png>)

### Port Scanner
(<screenshots/scanport.png>)

### Network Traffic Graph
(<screenshots/network traffic.png>)

---

## How to Run

1. Install dependencies

```bash
pip install numpy pandas scikit-learn matplotlib seaborn scapy

2. Generate Dataset

python generate_dataset.py

3. Train the Machine Learning Model

python train_model.py

4. Run the SOC Cybersecurity Dashboard

python security_dashboard.py


5. Test Attack Detection

Example normal traffic:

60,1,3,4000,3500,1400,40,30,9

Example attack traffic:

10,0,1,1200,300,500,5,3,1

6. Port Scanner

Enter target IP address:

127.0.0.1

or

192.168.1.1

7. IoT Device Discovery

Click Discover IoT Devices to detect active devices in the local network.

8. Network Traffic Visualization

Click Show Network Traffic Graph to visualize network activity.

Author

Aathila Fathima
B.Tech Final Year Project – Cybersecurity / Computer Science

