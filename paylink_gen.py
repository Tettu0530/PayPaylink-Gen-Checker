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
            try:
                amont = data_p2p["payload"]["pendingP2PInfo"]["amount"]
                print(f"{Color.GREEN}[SUCCESS] https://pay.paypay.ne.jp/{code} | Amount:{str(amont)} | {Color.GREEN}RESCODE:{str(get_p2p.status_code)} {Color.RESET}")
            except:
                print(f"{Color.GREEN}[SUCCESS] https://pay.paypay.ne.jp/{code} | {Color.GREEN}RESCODE:{str(get_p2p.status_code)} {Color.RESET}")
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
            print(f"{Color.RED}[FAILURE] https://pay.paypay.ne.jp/{code} | The URL dos not pending | {Color.GREEN}RESCODE:{str(get_p2p.status_code)} {Color.RESET}")
            return("died")
    except:
        print(f"{Color.RED}[FAILURE] https://pay.paypay.ne.jp/{code} | {Color.YELLOW}The URL does not exist | {Color.GREEN}RESCODE:{str(get_p2p.status_code)} {Color.RESET}")
        return("died")


os.system("cls")
os.system("title PayPayLinkGenerator-Checker Made by Tettu0530#0530-TuVoNeX#2214")

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

{Color.RESET}---------- Author:{Color.RED}Tettu0530#0530&TuVoNeX#2214{Color.RESET} ---------
-------------------- Version:{Color.RED}1.1.0{Color.RESET} --------------------
""")

amount = input(f"{Color.CYAN}How many links do you want to generate?:{Color.RESET}")
delay_gen = input(f"{Color.CYAN}Please input delay of generating urls. (0.001 is recommended.):{Color.RESET}")
yesno = input(f"{Color.CYAN}Do you want to check the PayPay link?(Y/N):{Color.RESET}")
print(f"Ganarating {str(amount)} of PayPay links...")

li = []
success = 0
failure = 0
total = 0

for i in range(int(amount)):
    link_i = rand_gen(16)
    link = "https://pay.paypay.ne.jp/" + link_i
    li.append(link)
    print(f"Successfully generated link : {link}")
    time.sleep(float(delay_gen))
with open(f"paylink.txt", "w", encoding="utf-8") as f:
    for i_ in li:
        f.write(f"{i_}\n")

if yesno == "Y" or yesno == "y":
    delay = input("Please input delay. (3 seconds is recommended.):")
    with open(f"paylink.txt", "r") as f:
        l = f.read().split("\n")
        paylink = ([i for i in l if i != ""])
        for i in paylink:
            result = check_link(i, "success_link.txt")
            time.sleep(int(delay))
            if result == "success":
                success += 1
            elif result == "died":
                failure += 1
        print(f"""
{Color.UNDERLINE}Successfully checked {str(success + failure)} URL.{Color.RESET}
{Color.GREEN}[SUCCESS] Total : {str(success)} URLS{Color.RESET}
{Color.RED}[FAILURE] Total : {str(failure)} URLS{Color.RESET}
        """)
        os.system("PAUSE")
else:
    print("exit application...")
    os.system("PAUSE")