import time
import sys
import os
import requests

# try import requests
try:
	from requests import *

except ImportError:
	fast("[!] requests module not installed ..")
	med("[*] wait a moment, this program will install the module ...")
	os.system("pip install requests")
	med("[*] done ...")

#clear function
def clear():
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('freebsd'):
        os.system('clear')
    else:
        os.system('cls')

# custom speed text
def slow(s):
    for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(10. / 100)

def med(s):
   for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(4. / 100)

def fast(s):
   for c in s + '\n' :
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(2. / 170)


def banner():
	print("""
 ____        _                     
/ ___| _   _| |__   ___ __ _ _ __  
\___ \| | | | '_ \ / __/ _` | '_ \ 
 ___) | |_| | |_) | (_| (_| | | | |
|____/ \__,_|_.__/ \___\__,_|_| |_|
 """)

clear()
banner()
med("""
=====================================================
[+] Subdomain Scanner by SystemofPekalongan       [+]
[+] Coded by root@x-krypt0n-x                     [+]
[+] Just a simple tools to make your life is easy [+]
[+] Thanks to : TXT, RST, KBH, Sy, MCX            [+]
===================================================== 
""")
print ("[!] enter your target without https: //")
print ("[!] example: site.com ")
target = input("[?] your target : ")
slow ("[+] searching subdomain ... \n")
time.sleep(1)

def main(target):
	url = "https://sonar.omnisint.io/subdomains/{}".format(target)
	data = requests.get(url).json()
	print ("[+] found : \n")
	for output in data:
		print(output)


main(target)
