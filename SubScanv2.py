# mengedit nama author dan mereupload nya dimana pun tidak akan mebuat mu jago kawan
# 18 - 19 4 21
import requests
import os
import sys
import time

try: 
    from requests import *

except ImportError:
    fast("[!] requests module not installed ..")
    med("[*] wait a moment, this program will install the module ...")
    os.system("pip install requests")
    med("[*] done ...")

def clear():
    if sys.platform.startswith('linux'):
        os.system('clear')
    elif sys.platform.startswith('freebsd'):
        os.system('clear')
    else:
        os.system('cls')

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
    ======================================================
    [+] Subdomain Scanner by SystemofPekalongan        [+]
    [+] Coded by root@x-krypt0n-x                      [+]
    [+] Just a simple tools to make your life is easy  [+]
    [+] Thanks to : TXT, AXS, KBH, Sy, MCX, SCD, SX77C [+]
    ====================================================== 
    """)

try:
    banner() 
    namefile = input("[?] want to save the subdoamin result file (Y/N): ").strip()
    sub = ("")

except KeyboardInterrupt:
    print("[!] you press ctrl + c")
    time.sleep(0.5)
    print("[!] exit")
    sys.exit(1)

def savefile(namefile):
    file = open((sub) + ".txt", "a")
    file.write(str(namefile))
    file.write("\n")
    file.close()

if namefile.startswith("y" or "Y"):
    print("[!] input file name without extension")
    sub = input("[?] enter the file name: ")
    savefile(namefile)
else: 
    print("[*] file not saved \n")

def subdo():
    try:
        print("[!] enter your target without https:// or http://")
        print("[!] example : site.com")
        target = input("[?] your target: ")
        slow("[+] searching subdomain ...\n")
        time.sleep(1)

        url = "https://sonar.omnisint.io/subdomains/{}".format(target)
        data = requests.get(url).json()
        for output in data:
            print("FOUND [*]", output)
            namefile = (output)
            
            savefile(namefile)

    except KeyboardInterrupt:
        print("[!] you press ctrl + c ...")
        print("[!] exit")
        sys.exit()

subdo()
