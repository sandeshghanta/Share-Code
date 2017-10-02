import os
import sys
import requests
filename = sys.argv[1]
flag = False
for i in (os.listdir(os.getcwd())):
    if (i == filename):
        flag = True
if (not flag):
    print filename + " file not found"
    exit(0)
falg = False
files = {'file': open(filename, 'rb')}
password = str(raw_input("Enter password for your file "))
if (password == ""):
    password = "null"
r = requests.post("http://sharecode.co.nf/server.php?filename="+filename+"&password="+password,files=files)
print r.text

