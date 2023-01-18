# -*- coding: utf-8 -*-
import os
import random

import requests
import ctypes
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
        "Accept": "application/json, text/plain, */*",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.76 Safari/537.36"
    }
    get_p2p = requests.get(
        f"https://www.paypay.ne.jp/app/v2/p2p-api/getP2PLinkInfo?verificationCode={code}&client_uuid={client_uuid}", headers=p2pinfo_headers)
    data_p2p = get_p2p.json()
    try:
        if data_p2p["payload"]["orderStatus"] == "PENDING":
            try:
                amont = data_p2p["payload"]["pendingP2PInfo"]["amount"]
                if data_p2p["payload"]["pendingP2PInfo"]["isSetPasscode"] == True:
                    print(
                        f"{Color.GREEN}[SUCCESS] https://pay.paypay.ne.jp/{code} | 金額t:{str(amont)} | {Color.GREEN}レスポンスコード:{str(get_p2p.status_code)} | {Color.RED}パスワード:あり {Color.RESET}")
                else:
                    print(
                        f"{Color.GREEN}[SUCCESS] https://pay.paypay.ne.jp/{code} | 金額:{str(amont)} | {Color.GREEN}レスポンスコード:{str(get_p2p.status_code)} | {Color.GREEN}パスワード:なし {Color.RESET}")
            except:
                print(
                    f"{Color.GREEN}[SUCCESS] https://pay.paypay.ne.jp/{code} | {Color.GREEN}レスポンスコード:{str(get_p2p.status_code)} {Color.RESET}")
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
                return ("success")
        else:
            print(
                f"{Color.RED}[FAILURE] https://pay.paypay.ne.jp/{code} | URLは無効です | {Color.GREEN}レスポンスコード:{str(get_p2p.status_code)} {Color.RESET}")
            return ("died")
    except:
        print(f"{Color.RED}[FAILURE] https://pay.paypay.ne.jp/{code} | {Color.YELLOW}URLは無効です | {Color.GREEN}レスポンスコード:{str(get_p2p.status_code)} {Color.RESET}")
        return ("died")


os.system("cls")
os.system("title PayPayLinkGenerator-Checker Made by Tettu0530#0530-TuVoNeX#2214")

def main():
    os.system("cls")
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

{Color.RESET}----------- 作者:{Color.RED}Tettu0530#0530&TuVoNeX#2214{Color.RESET} ----------
-------------------- Version:{Color.RED}1.2.1{Color.RESET} --------------------
    """)
    print("""
[1] PayPayLinkGenerator
[2] PayPayLinkChecker
[3] Exit
    """)
    number = input(f"[{Color.RED}!{Color.RESET}]モジュールを選択してください >")
    if number == "1":
        amount = input(
            f"{Color.CYAN}生成するリンク数:{Color.RESET}")
        delay_gen = input(
            f"{Color.CYAN}リンクを生成する間隔(推奨:0):{Color.RESET}")
        
        li = []

        for i in range(int(amount)):
            link_i = rand_gen(16)
            link = "https://pay.paypay.ne.jp/" + link_i
            li.append(link)
            print(f"リンクを生成しました : {link}")
            time.sleep(float(delay_gen))
        with open(f"paylink.txt", "w", encoding="utf-8") as f:
            for i_ in li:
                f.write(f"{i_}\n")
        time.sleep(1)
        print(f"{str(amount)} 個リンクを生成しました。")
        input("なんらかのキーを押すと終了します")
        main()
    elif number == "2":
        success = 0
        failure = 0
        total = 0
        file = input("リンクの入ったファイルの名前指定してください(例:link.txt)(空欄の場合はこのツールで生成したリンクがチェックされます):")
        if file == "":
                files = "paylink.txt"
        else:
            files = file
        if os.path.isfile(f"{files}") is True:
            delay = input("チェック間隔を設定してください(強く推奨:3以上):")
            with open(files, "r") as f:
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
{Color.UNDERLINE} {str(success + failure)} 個のリンクをチェックしました{Color.RESET}
{Color.GREEN}[SUCCESS] 合計: {str(success)} 個{Color.RESET}
{Color.RED}[FAILURE] 合計 : {str(failure)} 個{Color.RESET}
                """)
                enter = input("Enterキーを押すと終了します")
                if enter == "":
                    main()
        else:
            print(f"{Color.RED}[エラー]指定したファイル({files})は見つかりませんでした。{Color.RESET}")
            time.sleep(1)
            input("なんらかのキーを押すと終了します")
            main()

    elif number == "3":
        print("ツールを終了します...")
        os.system("PAUSE")
main()