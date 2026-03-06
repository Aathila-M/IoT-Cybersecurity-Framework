from scapy.all import sniff

packets = []

def packet_callback(packet):

    packets.append(len(packet))

def start_monitor():

    sniff(prn=packet_callback, count=50)