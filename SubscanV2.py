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
|____/ \__,_|_.__/ \___\__,_|_| |_| V2
    """)
    med("""
==========================================================
[+] Subdomain Scanner by SystemofPekalongan            [+]
[+] Coded by root@x-krypt0n-x                          [+]
[+] Just a simple tools to make your life is easy      [+]
[+] Thanks to : TXT, RST, AXS, KBH, Sy, MCX, SCD       [+]
========================================================== 
""")

try:
    clear()
    banner()
    namefile = input("\n[?] want to save the dork result file (Y/N) ").strip()
    sub = ("")

except KeyboardInterrupt:
    print("\n[!] you press ctrl + c")
    time.sleep(0.5)
    print("\n[!] exit")
    sys.exit(1)


def savefile(namefile):
    file = open((sub) + ".txt", "a")
    file.write(str(namefile))
    file.write("\n")
    file.close


if namefile.startswith("y" or "Y"):
    print("[!] input filename without extension")
    sub = input("[?] enter file name: ")
    savefile(namefile)
else:
    print("[*] file not saved\n")

def subdo():
    try: 
        print ("\n[!] enter your target without https: //")
        print ("[!] example: site.com ")
        target = input("[?] your target : ")
        slow ("[+] searching subdomain ... \n")
        time.sleep(1)

        url = "https://sonar.omnisint.io/subdomains/{}".format(target)
        data = requests.get(url).json()
        for output in data:
            time.sleep(0.5)
            print("FOUND [*]", output)
            namefile = (output)

            savefile(namefile)

    except KeyboardInterrupt:
        print("[!] you press ctrl + c")
        print("[!] exit")
        sys.exit()
subdo()
