#!/usr/bin/python3
"""
    Just a routine practice: Use subprocess module to ping a sequence of IP addresses, saving the output in a csv file.
"""
import subprocess as sp
import csv
import sys


IP     = "192.168.1"
try:
    MAX_IP = int(sys.argv[1])
except:
    MAX_IP = 1
ip_status = {}

# ping from 192.168.1.1 up to 192.168.1.MAX_IP
for i in range(1,MAX_IP+1):
  ip = IP+"."+str(i)
  status,result = sp.getstatusoutput(f"ping -c1 -w2 {ip}")
  if status == 0:
    print(f"{ip} is UP !")
    ip_status.update({ip:"up"})
  else:
    print(f"{ip} is DOWN !")
    ip_status.update({ip:"down"})
    
# Open in write mode the file, and put a header.
for ip,status in ip_status.items():
  try:
    with open('/tmp/ping_status.csv', mode='a+') as file:
      ping_status = csv.writer(file, delimiter =";")
      ping_status.writerow([ip,status])  
  except Exception as e:
    print(f"Error {e}")
