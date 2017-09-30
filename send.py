import requests
password = str(raw_input("Enter password press enter if no password is required"))
files = {'file': open('data1.txt', 'rb')}
if (password == ""):
    requests.post('http://sharecode.co.nf/server.php',files=files)
    print "file uploaded"
else:
    requests.post('http://sharecode.co.nf/server.php?password='+password,files=files)
    print "file uploaded"
    
