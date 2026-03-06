from scapy.all import sniff

def process_packet(packet):

    print(packet.summary())

def start_sniffing():

    print("Monitoring network traffic...")

    sniff(prn=process_packet,count=20)