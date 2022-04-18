# import os
# response = os.popen('ping -n 1 google.com')
# for line in response.readlines():
#     print(line)
    
from pythonping import ping
# response_list = ping('216.58.223.78', size=40, count=5)
# print(response_list)

target_hosts = ['nytimes.com',
            'github.com',
            'google.com',
            'reddit.com',
            'hashnode.com',
            'producthunt.com']

def ping_all(targets):
    for target in targets:
        print(ping(target, size=40, count=2))

# ping_all(target_hosts)       
    
