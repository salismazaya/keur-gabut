# coded by: salism3
# 15-01-2020

import requests
ses = requests.Session()
u = input("Username: ")
p = input("Password: ")
data = ses.post("https://mbasic.facebook.com/login", data={'email':u, 'pass':p, 'login':'submit'}).url
if "save-device" in data or "m_sess" in data or "home" in data:
	print()
	print(";".join([str(x).replace("<Cookie ", "").split(" ")[0] for x in ses.cookies]))
elif "checkpoint" in data:
	print("\nAkun Ente Checkpoint")
else:
	print("\nUsername / Password Salah")
