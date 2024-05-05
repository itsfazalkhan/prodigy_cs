from scapy.all import *
from prettytable import PrettyTable

# Create a table
table = PrettyTable(["Source IP", "Destination IP", "Protocol", "Payload"])

# Dictionary to map protocol numbers to names
protocol_names = {
    1: "ICMP",
    6: "TCP",
    17: "UDP",
    # Add more protocol numbers and their corresponding names as needed
}

def packet_callback(packet):
    if packet.haslayer(IP):
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol_number = packet[IP].proto

        # Get the protocol name from the dictionary or use "Unknown" if not found
        protocol_name = protocol_names.get(protocol_number, "Unknown")

        if packet.haslayer(TCP):
            payload = packet[TCP].payload
        elif packet.haslayer(UDP):
            payload = packet[UDP].payload
        else:
            payload = ""

        # Add packet information to the table
        table.add_row([src_ip, dst_ip, protocol_name, payload])

# Sniff packets
sniff(prn=packet_callback, store=0, count=20)

# Print the table
print(table)
