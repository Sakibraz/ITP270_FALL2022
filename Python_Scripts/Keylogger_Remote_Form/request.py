#!#!/usr/bin/env python3

import requests

url ='https://docs.google.com/forms/u/1/d/e/1FAIpQLSf0jT8Vq-jk-IDwS9Hw8uyjac99AVZCE5VM_7Zf2At4MniFfg/formResponse'

form_data = {'entry.839337160':'This is a test'}

r = requests.post(url, data=form_data)
