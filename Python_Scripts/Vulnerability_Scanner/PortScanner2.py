#!/usr/bin/env python3

import socket
from IPy import IP
import pyfiglet
import subprocess
import time

#//Clear the terminal window//
subprocess.call('clear', shell=True)

#//Port Scanner banner//
Port_Scanner_Banner = pyfiglet.figlet_format("PORT SCANNER")
print(Port_Scanner_Banner)

#//wait one second before proceeding//
time.sleep(1)

def scan(target) :
	'''//scan target function//'''
	converted_ip = convert_ip(target)
	print('/n' + 'Scanning Target : ' + str(target))
	for port in range(21,500):
		scan_port(converted_ip, port)

def convert_ip(ip):
	'''//Function converts the hostname if not already an IP//'''
	try:
		IP(ip)
		return(ip)
	except ValueError:
		return socket.gethostbyname(ip)

def get_banner(s):
	'''//function grabs any port banner and returns the data received//'''
	return s.recv(1024)


def scan_port(ipaddress, port):
	'''//function scans PORTS of the target and sets the connection
timeout to 0.5 to connect (faster but not as accurate increase number
for better accuracy) >> If there is a banner, Collect the port banner,
strip out the unwanted characters, and print to the terminal window >>
If no port banner print open port >> If port is closed pass (print
nothing to the terminal)//'''
	try:
		sock = socket.socket()
		sock.settimeout(0.5)
		sock.connect((ipaddress, port))

		try:
			banner = get_banner(sock)
			print('[+] Port ' + str(port) + ' is Open ' + ' : ' + str(banner.decode().strip('\n')))
		except:
			print('[+] Port ' + str(port) + ' is Open ')
	except:
		pass

#//Scan multiple targets specified with a comma else scan one specified target//
#//Line 55 prevents the scan function from being called twice if the script is imported into another module//
if __name__ == "__main__":
	targets = input('[+] Enter Target/s To Scan(for multiple targets use a comma): ')
	if ',' in targets:
		for ip_address in targets.split(','):
			scan(ip_address.strip(' '))
	else:
		scan(targets)
