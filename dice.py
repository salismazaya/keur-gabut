#coded by: salism3
#11-09-2019

import os
from random import randint as kocok
h = "\033[92m"
p = "\033[0m"

def dadu():
	total = 0
	while True:
		total += 1
		os.system('clear')
		print("[ Dice Roller ]")
		a = kocok(1,6)
		b = kocok(1,6)
		print("\n[+] Roll ke: " + str(total))
		if a == b:
			print("[+] Hasil: " + h + "Double " + str(a + b) + p)
		else:
			print("[+] Hasil: " + h + str(a + b) + p)
		rool = str(input("[?] Roll lagi (y/n): ")).upper()
		if rool == "N":
			exit("[!] Program Berhenti")
		
try:
	dadu()
except Exception as e:
	print("[!] " + str(e))
