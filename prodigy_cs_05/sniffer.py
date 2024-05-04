from scapy.all import *

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = packet[IP].proto

        print(f"Source IP: {src_ip} | Destination IP: {dst_ip} | Protocol: {protocol}")

        if packet.haslayer(TCP):
            payload = packet[TCP].payload
            print(f"TCP Payload: {payload}")
        elif packet.haslayer(UDP):
            payload = packet[UDP].payload
            print(f"UDP Payload: {payload}")

sniff(prn=packet_callback, store=0)
