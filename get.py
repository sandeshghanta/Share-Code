import os
import sys
import requests
filename = sys.argv[1] 
password = str(raw_input("Enter the password for the file"))
if (password == ""):
    password = "null"
r = requests.post("http://sharecode.co.nf/getcode.php?filename="+filename+"&password="+password+"&getname=true")
localname = r.text
r = requests.post("http://sharecode.co.nf/getcode.php?filename="+filename+"&password="+password)
if (r.text == "False"):
    print "Wrong combination of filename and password"
    exit(0)
flag = True
for i in os.listdir(os.getcwd()):
	if (i == localname):
		print "A file with the name " + localname + " already exists"
		newname = str(raw_input("Enter new file name "))
		if (newname != ""):
			localname = newname
		break
file = open(localname,'w+')
file.write(r.text)
file.close()

