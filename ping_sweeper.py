import subprocess

network="10.10.50."
IPs = []

for host in range(1,255):
    IP = network + str(host)
    
    process = subprocess.run('ping -c 1 -w 1 '+ IP,stdout=subprocess.PIPE, shell=True)
  
    if process.returncode == 0:
        IPs.append(IP)
        print(f" {IP} IS ALIVE !! ")
        
print(f"Ping completed successfully & there are {len(IPs)} IPs hosts!")



# import ipaddress

# mynet = ipaddress.ip_network('192.168.0.0/16') 
# for host in mynet.hosts():                    
#     host = str(host)
#     print(host)  
      
    