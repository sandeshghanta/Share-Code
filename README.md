# Share-Code

[![Join the chat at https://gitter.im/sandeshghanta/Share-Code](https://badges.gitter.im/sandeshghanta/Share-Code.svg)](https://gitter.im/sandeshghanta/Share-Code?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

A python script which can be run from the command line to share code with your friends.Presently this works only in Windows

Installation
This script requires the python module 'requests' to work. So install requests by the running the following command 'pip install requests'.
Next check whether the python path is there or not. A simple test is to open command prompt and enter pip.If pip is working it means that the path is already modified so we need not make any changes to it. However if the command not found error arises then we need to add python to the path. Adding python to the path is pretty easy you can google the same and do it.
Then download the Share-Code repository and copy the files 'get.py' and 'send.py' to the following location 'C:/Python27/Scripts/'. You can delete the all the remaining files in the 'Share-Code' repository.
The installation is complete

Usage
Sending the Code
To share code with your friends open cmd and cd to the location where your code is present. Then run the following command 'send.py' followed by the name of your file. 
You will be asked to enter a password this is if you protect your files. If you do not want to have a password for your file just press enter. 
After the file is uploaded a random string with 5 characters will be generated. You need to share the string and the password if any to your friend who wants your code

Getting the Code
To download the code open cmd and cd to the location where you want your code to be downloaded. Then run the command 'get.py' followed by the random string which your friend shared with you. You will be asked to enter a password. If there is a password enter it or else press enter.
Your file shall be downloaded.

Version-2
I am planning to include new features like adding an option to share entire directories instead of just files. Make the code also compatible in ubuntu. Make a website such that code can be uploaded in a webpage and also the ability for a user to download the code through a browser
If there are any bugs or if you want to contribute to this project please contact me.

