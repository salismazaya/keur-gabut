# pake python3 ya mamank
# key ganti sendiri
# cara generate key
# import os;print(os.urandom(16))

class modol:
	def __init__(self, x): 
		# ini key
		self.key = b'\x19\r\xe64.\xb0\x93\xe9\x8d.\x83\x032?\xe6{'
		self.x = x
	
	def enc(self):
		teks = self.x
		a = pyaes.AESModeOfOperationCTR(self.key)
		b = a.encrypt(teks)
		c = compress(b)
		return str(b64encode(c)).split("'")[1]
	
	def dec(self):
		try:
			teks = self.x
			f = pyaes.AESModeOfOperationCTR(self.key)
			a = b64decode(teks)
			b = decompress(a)
			return str(f.decrypt(b)).split("'")[1]
		except:
			return "not found"

def home():
	os.system('clear')
	print("[ Teks Encrypt / Decyrpt ]")
	print("[ Coded by: SalisM3 ]\n")
	print("1). Encrypt")
	print("2). Decrypt\n")
	pilih = int(input('[?] Pilih >>> '))
	if pilih == 1:
		teks = str(input('[?] Teks: '))
		a = modol(teks)
		out = a.enc()
		print("[+] Output: " + str(out))
	elif pilih == 2:
		teks = str(input('[?] Teks: '))
		a = modol(teks)
		out = a.dec()
		print("[+] Output: " + str(out))

try:
	from base64 import *
	from zlib import *
	import os, pyaes
	home()
except ImportError:
	print("[+] pip install pyaes")
except KeyboardInterrupt:
	print("[!] Exit: Ok")
except Exception as e:
	print("[!] " + str(e))
