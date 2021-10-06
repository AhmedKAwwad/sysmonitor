from random import choice
import string
from tabulate import tabulate

def create_dev(num_devices,num_subnets):
   
   devices = list()
   if num_devices>254 or num_subnets>254:
      print("Error: too many devices and/or subnets requested")
      return devices
   for subnet_index in range(1,num_subnets+1):
      
      for device_index in range(1,num_devices+1):
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
         device["ip"] = "10.0." + str(subnet_index)+"."+ str(device_index)

         # NICELY FORMATED PRINT OF EACH DEVICE
         print()
         for key, value in device.items():
            print(f"{key:>15s}:{value}")
         # Add each device to list
         devices.append(device)
   return devices


if __name__ == '__main__':
   devices,s = create_dev(5,3)
   print("\n",tabulate(devices,headers="keys"))
   print(s)

