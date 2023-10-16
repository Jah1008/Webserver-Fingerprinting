import os
import requests

print("\nWebserver fingerprinting ")
server = input("Server name: ")
req = requests.get('http://www.' + server)
print("\nBanner Grab")
print(req.headers)
print()

some_headers = ['Server', 'Date', 'Via', 'X-Powered-By', 'ETag']
for header in some_headers:
    try:
        res = req.headers[header]
        print(header + " : " + res)
    except:
        print(header + " : Not found")

try:
    print("\nProbable Server Type")
    info = list(req.headers)
    for i in range(len(info)):
        if(info[i]=='Date' or info[i]=='date'):
            d=i
        if(info[i]=='Server' or info[i]=='server'):
            s=i

    if(d>s):
        print("Might be Apache\n")
    else:
        print("Might be IIS/Netscape\n")
except:
    print("Could not find probable server type\n")
