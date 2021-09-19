from random import choice
import string
from tabulate import tabulate
from operator import itemgetter
from pprint import pprint

devices = list()

# FOR LOOP to create LARGE NUMBER OF DEVICES
for index in range(1,10):
   # Create device
   device = dict()
   # RANDOM DEVICE NAME
   device ["name"] = (
      choice(["r2","r3","r4","r6","r18"])
      + choice(["L","U"])
      + choice(string.ascii_letters)
   )
   # Random Vendor
   device["vendor"] = choice(["cisco","juniper","arista"])
   if device["vendor"]== "cisco":
      device["os"] =choice(["ios","iosxe","iosxr","nexus"])
      device["version"] =choice(["12.1(T).84","14.87x","8.12(s)"])
   elif device["vendor"] == "juniper":
      device["os"] =choice(["junos"])
      device["version"] =choice(["12.1(S).84","14.87S","8.12(T)"])
   elif device["vendor"] == "arista":
      device["os"] =choice(["eos"])
      device["version"] =choice(["12.1(E).84","14.87E","8.12(E)"])
   device["ip"] = "10.0.0" + str(index)

   # NICELY FORMATED PRINT OF EACH DEVICE
   print()
   for key, value in device.items():
      print(f"{key:>15s}:{value}")
   # Add each device to list
   devices.append(device)


# Print DATA AS-IS
print ("\n------- Device As lIST OF DICTS ------------")
pprint(devices)

# Print use 'TABULATE' 
print ("\n------- Print Device As Table ------------")
sorted_tabulate=sorted(devices,key=itemgetter("vendor","os","version"))
print(tabulate(sorted_tabulate,headers="keys"))

