print(" *******************")

print(" *******************")

print(" KNOW YOUR IP TOOL BY ARBHS")

print(" Instagram : kethiri_anon ")

print(" *******************")

print(" *******************")

#!/usr/bin/python

import requests

url = 'http://api.ipify.org/'

response = requests.get(url)

ip=response.text

print("Your IP Address is :" + ip)
