import pandas as pd
import random

rows = []

for i in range(50000):

    duration = random.randint(1,60)
    protocol = random.choice(["tcp","udp","icmp"])
    service = random.choice(["http","ftp","ssh","dns"])

    src_bytes = random.randint(100,5000)
    dst_bytes = random.randint(50,4000)

    packet_size = random.randint(100,1500)
    src_packets = random.randint(1,50)
    dst_packets = random.randint(1,50)

    login_attempts = random.randint(0,10)

    # attack logic
    if src_bytes > 3000 and dst_bytes > 2000:
        attack = "attack"
    elif login_attempts > 5:
        attack = "attack"
    elif src_packets > 35:
        attack = "attack"
    else:
        attack = "normal"

    rows.append([
        duration,protocol,service,src_bytes,dst_bytes,
        packet_size,src_packets,dst_packets,login_attempts,attack
    ])

df = pd.DataFrame(rows,columns=[
"duration","protocol","service","src_bytes","dst_bytes",
"packet_size","src_packets","dst_packets","login_attempts","attack_type"
])

df.to_csv("dataset/iot_attack_dataset.csv",index=False)

print("Dataset generated successfully")