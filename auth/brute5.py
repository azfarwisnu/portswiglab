import requests
from bs4 import BeautifulSoup

'''
 Your credentials: wiener:peter
Victim's username: carlos 
'''

url = "https://0a78009a04128edcc110169e00bb003a.web-security-academy.net/login"
username = "wiener"
password = open("password.txt","r").readlines()
new_pas = []
index  = 1

for pas in password:
	pas = pas.replace("\n","")
	pas = f'"{pas}",'
	print(pas)
	new_pas.append(pas)