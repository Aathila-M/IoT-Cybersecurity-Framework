import tkinter as tk
from tkinter import messagebox, ttk
import matplotlib.pyplot as plt
import threading

from intrusion_detection import predict_attack
from port_scanner import scan_ports
from device_scanner import discover_devices
from packet_monitor import packets

# window

window = tk.Tk()
window.title("IoT Cybersecurity SOC Dashboard")
window.geometry("1000x700")
window.configure(bg="#0f172a")

title = tk.Label(
    window,
    text="IoT Cybersecurity Security Operations Center",
    font=("Arial",22,"bold"),
    fg="white",
    bg="#0f172a"
)

title.pack(pady=15)

# attack detection

frame1 = tk.Frame(window,bg="#1e293b",padx=20,pady=20)
frame1.pack(pady=10)

tk.Label(frame1,text="Enter Network Features",bg="#1e293b",fg="white").pack()

entry = tk.Entry(frame1,width=40)
entry.pack(pady=5)

def threat_level(result):

    if result == 0:
        return "LOW"
    elif result == 1:
        return "MEDIUM"
    else:
        return "HIGH"

def detect_attack():

    try:

        features = list(map(int,entry.get().split(",")))

        result = predict_attack(features)

        level = threat_level(result)

        if level == "LOW":

            messagebox.showinfo("Status","Normal Traffic")

        else:

            messagebox.showwarning(
                "Alert",
                f"⚠ Cyber Attack Detected\nThreat Level: {level}"
            )

            status_label.config(text="⚠ THREAT DETECTED",fg="red")

    except:

        messagebox.showerror("Error","Invalid input")

tk.Button(
    frame1,
    text="Detect Attack",
    bg="#2563eb",
    fg="white",
    command=detect_attack
).pack(pady=5)

# port scanner

frame2 = tk.Frame(window,bg="#1e293b",padx=20,pady=20)
frame2.pack(pady=10)

tk.Label(frame2,text="Enter Target IP",bg="#1e293b",fg="white").pack()

ip_entry = tk.Entry(frame2)
ip_entry.pack(pady=5)

progress = ttk.Progressbar(frame2,length=200)
progress.pack(pady=5)

columns = ("Port","Service")

table = ttk.Treeview(window,columns=columns,show="headings",height=6)

table.heading("Port",text="Port")
table.heading("Service",text="Service")

table.pack(pady=10)

def run_scan():

    ip = ip_entry.get()

    table.delete(*table.get_children())

    progress["value"] = 0

    results = scan_ports(ip)

    for port,service in results:

        table.insert("", "end", values=(port,service))

    progress["value"] = 100

tk.Button(
    frame2,
    text="Scan Ports",
    bg="#16a34a",
    fg="white",
    command=lambda: threading.Thread(target=run_scan).start()
).pack(pady=5)

# traffic graph

def show_graph():

    traffic = [10,20,30,25,40,50]

    plt.style.use("dark_background")

    plt.plot(traffic)

    plt.title("Network Traffic Graph")

    plt.show()

tk.Button(
    window,
    text="Show Network Traffic Graph",
    bg="#9333ea",
    fg="white",
    command=show_graph
).pack(pady=10)

# device discovery

def scan_devices():

    devices = discover_devices()

    messagebox.showinfo("Devices Found",str(devices))

tk.Button(
    window,
    text="Discover IoT Devices",
    bg="#f59e0b",
    fg="black",
    command=scan_devices
).pack(pady=10)

# SOC status

status_frame = tk.Frame(window,bg="#1e293b",padx=20,pady=20)
status_frame.pack(pady=10)

tk.Label(
    status_frame,
    text="SOC Security Status",
    bg="#1e293b",
    fg="white",
    font=("Arial",14,"bold")
).pack()

status_label = tk.Label(
    status_frame,
    text="SYSTEM SECURE",
    bg="#1e293b",
    fg="#22c55e"
)

status_label.pack()

window.mainloop()