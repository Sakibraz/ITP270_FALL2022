#!/usr/bin/env python3

import socket
import subprocess
import time
import sys
import pyfiglet

subprocess.call('clear', shell=True)

Port_Scanner_Banner = pyfiglet.figlet_format("ITP270 - PORT SCANNER")
print(Port_Scanner_Banner)

time.sleep(1)

remoteServer = input("Enter a IP to scan: ")
target = socket.gethostbyname(remoteServer)

print("_" * 50)
print("Scanning the following Host: " + target)
print("_" * 50)

try:

	for port in range (1,4000):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		result = s.connect_ex((target, port))
		if result ==0:
			print("Port {}: is open".format(port))
		s.close()


except KeyboardInterrupt:
	print("\n The Scan Was Canceled")
	sys.exit()

except socket.gaierror:
	print("\n Hostname Could Not Be Resolved")
	sys.exit()

except socket.error:
	print("\n No response")
	sys.exit()
