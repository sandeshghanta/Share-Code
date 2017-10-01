import os
import sys
import requests
filename = sys.argv[0]
password = str(raw_input("Enter the password for the file"))
if (password == ""):
    password = "null"
r = requests.get("http://sharecode.co.nf/files?filename="+filename+"&password="+password)
if (r.text == "False"):
    print "Wrong combination of filename and password"
    exit(0)
print 
