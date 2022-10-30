import os
import random
import sys
from turtle import color

import requests
import ctypes
import datetime
import uuid
import time

ENABLE_PROCESSED_OUTPUT = 0x0001
ENABLE_WRAP_AT_EOL_OUTPUT = 0x0002
ENABLE_VIRTUAL_TERMINAL_PROCESSING = 0x0004
MODE = ENABLE_PROCESSED_OUTPUT + ENABLE_WRAP_AT_EOL_OUTPUT + \
    ENABLE_VIRTUAL_TERMINAL_PROCESSING

kernel32 = ctypes.windll.kernel32
handle = kernel32.GetStdHandle(-11)
kernel32.SetConsoleMode(handle, MODE)


class Color:
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    COLOR_DEFAULT = '\033[39m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    INVISIBLE = '\033[08m'
    REVERCE = '\033[07m'
    BG_BLACK = '\033[40m'
    BG_RED = '\033[41m'
    BG_GREEN = '\033[42m'
    BG_YELLOW = '\033[43m'
    BG_BLUE = '\033[44m'
    BG_MAGENTA = '\033[45m'
    BG_CYAN = '\033[46m'
    BG_WHITE = '\033[47m'
    BG_DEFAULT = '\033[49m'
    RESET = '\033[0m'


def rand_gen(n):
    STRING = "A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P,Q,R,S,T,U,V,W,X,Y,Z,0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z".split(
        ",")
    return "".join(random.choice(STRING) for i in range(n))

def check_link(code_i, file):
    code = code_i.replace("https://pay.paypay.ne.jp/", "")
    client_uuid = str(uuid.uuid4())
    p2pinfo_headers = {
        "Accept":"application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"
    }
    get_p2p = requests.get(f"https://www.paypay.ne.jp/app/v2/p2p-api/getP2PLinkInfo?verificationCode={code}&client_uuid={client_uuid}", headers=p2pinfo_headers)
    data_p2p = get_p2p.json()
    try:
        if data_p2p["payload"]["orderStatus"] == "PENDING":
            print(f"{Color.GREEN}[SUCCESS]https://pay.paypay.ne.jp/{code}{Color.RESET}")
        try:
            with open(f"{file}.txt", "r", encoding="utf-8") as f:
                content = f.read()
        except:
            content = ""
            with open(f"{file}.txt", "a", encoding="utf-8") as f:
                if content == "":
                    f.write(f"https://pay.paypay.ne.jp/{code}")
                else:
                    f.write(f"\nhttps://pay.paypay.ne.jp/{code}")
                return("success")
        else:
            print(f"{Color.RED}[FAILURE]https://pay.paypay.ne.jp/{code} The URL dos not pending{Color.RESET}")
            return("died")
    except:
        print(f"{Color.RED}[FAILURE]https://pay.paypay.ne.jp/{code} The URL does not exist{Color.RESET}")
        return("died")


os.system("cls")
os.system("title PayPayLinkGenerator-Checker Made by Tettu0530#0530")

print(Color.BLUE + f"""  _____            _____            _      _       _                
 |  __ \          |  __ \          | |    (_)     | |               
 | |__) __ _ _   _| |__) __ _ _   _| |     _ _ __ | | __            
 |  ___/ _` | | | |  ___/ _` | | | | |    | | '_ \| |/ /            
 | |  | (_| | |_| | |  | (_| | |_| | |____| | | | |   <             
 |_|   \__,_|\__, |_|   \__,_|\__, |______|_|_| |_|_|\_\            
              __/ |            __/ |                                
   _____     |___/            |______ _               _             
  / ____|              ___     / ____| |             | |            
 | |  __  ___ _ __    ( _ )   | |    | |__   ___  ___| | _____ _ __ 
 | | |_ |/ _ | '_ \   / _ \/\ | |    | '_ \ / _ \/ __| |/ / _ | '__|
 | |__| |  __| | | | | (_>  < | |____| | | |  __| (__|   |  __| |   
  \_____|\___|_| |_|  \___/\/  \_____|_| |_|\___|\___|_|\_\___|_|  

{Color.RESET}Author:{Color.RED}Tettu0530#0530{Color.RESET}
Version:{Color.RED}1.0.0{Color.RESET}
""")

amont = input("How many links do you want to generate?:")
yesno = input("Do you want to check the PayPay link?(Y/N):")
print(f"Ganarating {str(amont)} of PayPay links...")
list = []
for i in range(int(amont)):
    link_i = rand_gen(16)
    link = "https://pay.paypay.ne.jp/" + link_i
    list.append(link)
    print(f"Successfully generated link : {link}")
with open(f"paylink.txt", "w", encoding="utf-8") as f:
    f.write(str(list))

if yesno == "Y" or yesno == "y":
    delay = input("Please input delay (3 seconds is recommended.):")
    paylink = ([i for i in list if i != ""])
    for i in paylink:
        check_link(i, "success_link.txt")
        time.sleep(int(delay))
    print(f"""
Successfully checked {len(link)} URL.
    """)
    os.system("PAUSE")
else:
    print("exit application...")
    os.system("PAUSE")