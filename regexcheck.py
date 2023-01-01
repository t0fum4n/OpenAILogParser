import re

# Define the regex pattern
pattern = r"\|srcIP=(.*?)\|srcPort=(.*?)\|srcMAC=(.*?)\|dstIP=(.*?)\|dstPort=(.*?)\|"

# Define the string to check
string = "Tue Mar 04 15:57:06 2020: <14>Mar  4 15:53:03 BAR-NG-VF500 BAR-NG-VF500/box_Firewall_Activity:  Info     BAR-NG-VF500 Remove: type=FWD|proto=UDP|srcIF=eth1|srcIP=192.168.70.7|srcPort=35119|srcMAC=08:00:27:da:d7:9c|dstIP=8.8.8.8|dstPort=53|dstService=domain|dstIF=eth0|rule=InternetAccess/<App>:RestrictTim|info=Balanced Session Idle Timeout|srcNAT=192.168.70.7|dstNAT=8.8.8.8|duration=21132|count=1|receivedBytes=130|sentBytes=62|receivedPackets=1|sentPackets=1|user=|protocol=|application=|target=|content=|urlcat"

# Check if the string matches the regex pattern
match = re.match(pattern, string)

# If the match is not None, the string matches the pattern
if match:
    print("The string matches the pattern.")
else:
    print("The string does not match the pattern.")