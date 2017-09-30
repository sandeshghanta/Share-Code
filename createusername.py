import sys
import requests
username = sys.argv[1]
url = "http://sharecode.co.nf/createusername.php?username="+username
r = requests.post(url)
print r.text
