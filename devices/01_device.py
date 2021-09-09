from pprint import pprint

# Dic repsenting a device
device = {
  "name":"D01-Host",
  "vendor":"Gigabyte",
  "model":"B150",
  "os":"Win10",
  "version":"HD3",
  "ip":"127.0.0.1" 
}

# simple print
print("\n ________Simple Print______")
print("device: ",device)
print("device name: ",device["name"])

# PRETTY PRINT
print("\n ________Pretty Print______")
print("device: ")
pprint(device)

