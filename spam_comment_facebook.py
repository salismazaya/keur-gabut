# coded by: salism3
# 11 - 04 - 2020
# use python3

import mechanize, time

print("\t\t[ FB Comment Spammer ]\n")

br = mechanize.Browser()
br.set_handle_robots(False)

kuki = input("[?] Your Facebook Cookies: ")
br.addheaders = []
br.addheaders.append(("User-Agent", "Mozilla/5.0 (Linux; Android 8.1.0; Redmi 5A Build/OPM1.171019.026; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.99 Mobile Safari/537.36"))
br.addheaders.append(("cookie", kuki))

if "mbasic_logout_button" in br.open("https://mbasic.facebook.com").read().decode():
	print("[+] Login Sukses")
else:
	exit("[+] Cookies Tidak Valid")

for _ in range(20):
	print("[!] ex: https://mbasic.facebook.com/photo.php?fbid=166694224710808&id=100041106940465")
	url = input("[?] url to post (use mbasic): ")
	try:
		if not "https://mbasic.facebook.com":
			raise Exception
		html = br.open(url).read().decode()
		if "Konten Tidak Ditemukan" in html:
			raise Exception
		break
	except:
		print("[!] Url Tidak Valid / Post Tidak Ditemukan")
else:
	exit("[!] Dah Lah Malesss")

text = input("[?] isi komentar: ")
for _ in range(int(input("[?] jumlah komentar: "))):
	br.open(url)
	br.select_form(nr=0)
	br["comment_text"] = text
	br.submit()
	print("Ok")
	time.sleep(1.1)
