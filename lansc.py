#!/usr/bin/python
import os
import time
from tabulate import tabulate

time.sleep(1)
gw = os.popen("ip route | grep / | awk '{print $1}'").read()
print("Starting LAN Scanner v1.0 (Powered by Nmap) (https://github.com/zexceed12300)")
print("Scanning for GATEWAY "+gw)
sc_data0 = os.popen("nmap $(ip route | grep / | awk '{print $1}')").read()
sc_data1 = os.popen("nmap $(ip route | grep / | awk '{print $1}') -sP -n ").read()
a = open("./.sc_data0.txt","w")
a.write(sc_data0)
a.close()
b = open("./.sc_data1.txt","w")
b.write(sc_data1)
b.close()

ip = os.popen("grep report ./.sc_data1.txt | awk '{print $5}'").read()
mac = os.popen("grep MAC ./.sc_data1.txt | awk '{print $3}'").read() + os.popen("ip addr | grep 'state UP' -A1 | tail -n1 | awk '{print $2}' | cut -f1 -d'/'").read()
hostnames = os.popen("grep 'Nmap scan' ./.sc_data0.txt | awk '{print $5}'").read()
manufacturer = os.popen("grep MAC ./.sc_data1.txt | awk '{print $4, S$5 $6}'").read() + "(This Devices)"

tables = [
        ["IP Address","MAC Address","Hostnames","Manufacturer"],
        [ip,mac,hostnames,manufacturer]
]

print(tabulate(tables,headers='firstrow'))
