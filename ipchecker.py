#Enter the file name into the with open space
with open('Allowed user list\IPAllowList.txt','r') as file:
    valid_ip_addresses = file.readlines()


#Rnter the Flagged Ips here
flagged_addresses = ["192.168.190.178", "192.168.96.200", "192.168.174.117", "192.168.168.144"]

for line in valid_ip_addresses:

  
    if line in flagged_addresses:
        print("The IP address", line, "has been flagged for further analysis.")
  
    else:
        print("The IP address", line, "does not require further analysis.")
