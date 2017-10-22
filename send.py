import os
import sys
import requests


def main() {
   filename = sys.argv[1]
   flag = False

   for i in (os.listdir(os.getcwd())):
       if (i == filename):
           flag = True
           break

   if (not flag):
       print filename + " file not found"
       exit(0)

   flag = False
   files = {'file': open(filename, 'rb')}
   password = str(raw_input("Enter password for your file "))

   if (password == ""):
       password = "null"
   r = requests.post("http://sharecode.co.nf/server.php?filename="+filename+"&password="+password,files=files)
   print r.text
}


if __name__ == "__main__":
   main()