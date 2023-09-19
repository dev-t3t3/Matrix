import os
import json
import time
import subprocess
import datetime
from requests import get

try:
    import requests
except ModuleNotFoundError:
    os.system('pip install requests')
try:
    import colorama
except ModuleNotFoundError:
    os.system('pip install colorama')
try:
    import fade
except ModuleNotFoundError:
    os.system('pip install fade')
try:
    import socket
except ModuleNotFoundError:
    os.system('pip install socket')
try:
    import threading
except ModuleNotFoundError:
    os.system('pip install threading')
    
from colorama import *
from fade import *

myip=get("https://api.ipify.org").text

with open("settings.json") as config:
    config = json.load(config)
    theme = config["Theme_Color"]
    User = config["User"]

now = datetime.datetime.utcnow()
d2 = datetime.datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

banner = f"""
                                                                                                                 
                ███╗   ███╗ █████╗ ████████╗██████╗ ██╗██╗  ██╗
                ████╗ ████║██╔══██╗╚══██╔══╝██╔══██╗██║╚██╗██╔╝
                ██╔████╔██║███████║   ██║   ██████╔╝██║ ╚███╔╝ 
                ██║╚██╔╝██║██╔══██║   ██║   ██╔══██╗██║ ██╔██╗ 
                ██║ ╚═╝ ██║██║  ██║   ██║   ██║  ██║██║██╔╝ ██╗
                ╚═╝     ╚═╝╚═╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝
                                            
"""

if theme == "yellow":
    faded_text = fade.fire(banner)
    shr6h = f"{Fore.RESET}[{Fore.YELLOW}>{Fore.RESET}]"
    number1 = f"{Fore.LIGHTYELLOW_EX}1"
    number2 = f"{Fore.LIGHTYELLOW_EX}2"
    number3 = f"{Fore.LIGHTYELLOW_EX}3"
    number4 = f"{Fore.LIGHTYELLOW_EX}4"
    number5 = f"{Fore.LIGHTYELLOW_EX}5"
    number6 = f"{Fore.LIGHTYELLOW_EX}6"
    chose = f"{Fore.YELLOW}"

if theme == "green":
    faded_text = fade.brazil(banner)
    shr6h = f"{Fore.RESET}[{Fore.GREEN}>{Fore.RESET}]"
    number1 = f"{Fore.LIGHTGREEN_EX}1"
    number2 = f"{Fore.LIGHTGREEN_EX}2"
    number3 = f"{Fore.LIGHTGREEN_EX}3"
    number4 = f"{Fore.LIGHTGREEN_EX}4"
    number5 = f"{Fore.LIGHTGREEN_EX}5"
    number6 = f"{Fore.LIGHTGREEN_EX}6"
    chose = f"{Fore.GREEN}"

if theme == "red":
    faded_text = fade.pinkred(banner)
    shr6h = f"{Fore.RESET}[{Fore.RED}>{Fore.RESET}]"
    number1 = f"{Fore.LIGHTRED_EX}1"
    number2 = f"{Fore.LIGHTRED_EX}2"
    number3 = f"{Fore.LIGHTRED_EX}3"
    number4 = f"{Fore.LIGHTRED_EX}4"
    number5 = f"{Fore.LIGHTRED_EX}5"
    number6 = f"{Fore.LIGHTRED_EX}6"
    chose = f"{Fore.RED}"

if theme == "default":
    faded_text = fade.purplepink(banner)
    shr6h = f"{Fore.RESET}[{Fore.MAGENTA}>{Fore.RESET}]"
    number1 = f"{Fore.LIGHTMAGENTA_EX}1"
    number2 = f"{Fore.LIGHTMAGENTA_EX}2"
    number3 = f"{Fore.LIGHTMAGENTA_EX}3"
    number4 = f"{Fore.LIGHTMAGENTA_EX}4"
    number5 = f"{Fore.LIGHTMAGENTA_EX}5"
    number6 = f"{Fore.LIGHTMAGENTA_EX}6"
    chose = f"{Fore.MAGENTA}"


def portscanner(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((host, port))
        print(f"{Fore.LIGHTGREEN_EX}[+] Port ({port}) is open!")
        sock.close()
    except:
        pass

def portsc():
    os.system('cls')
    os.system(f'title Matrix Protection - Port Scanner - Theme: {theme}')
    print(faded_text)
    print()
    host = input(f"{shr6h} {Fore.RESET}Enter the host to scan: ")
    print(f"{Fore.LIGHTBLUE_EX}Starting Scanner.\n")
    print()
    for port in range(1, 65536):
        t = threading.Thread(target=portscanner, args=(host, port))
        t.start()
    print()
    print(f"{shr6h} {Fore.RESET}FINISHED")
    time.sleep(3)
    menu()

def pinger():
    os.system('cls')
    os.system(f'title Matrix - Pinger - Theme: {theme}')
    print(faded_text)
    print()
    host = input(f"{shr6h} {Fore.RESET}Enter the host to scan: ")
    response_times = []
    for i in range(4):
        response = subprocess.run(['ping', '-n', '1', host], stdout=subprocess.PIPE)
        response_time = response.stdout.decode().split(" = ")[-1].split("ms")[0]
        response_times.append(float(response_time))
    for i in range(4):
        print(f"{Fore.RESET}IP: {Fore.GREEN}{host} {Fore.RESET}PING: {Fore.GREEN}{response_times[i]}ms")
    
    print()
    print(f"{shr6h} {Fore.RESET}FINISHED")
    time.sleep(3)
    menu()    
    
def info():
    os.system('cls')
    os.system(f'title Matrix - Domain Info - Theme: {theme}')
    print(faded_text)
    print()
    domain = input(f"{shr6h} {Fore.RESET}Enter the IP to scan: ")
    url = "http://ip-api.com/json/" + domain
    response = requests.get(url)
    data = response.json()
    print()
    print(f"{Fore.GREEN}[+] Status:{Fore.RESET}", data["status"])
    print(f"{Fore.GREEN}[+] Continent:{Fore.RESET}", data["timezone"])
    print(f"{Fore.GREEN}[+] Country:{Fore.RESET}", data["country"])
    print(f"{Fore.GREEN}[+] CountryCode:{Fore.RESET}", data["countryCode"])
    print(f"{Fore.GREEN}[+] ISP:{Fore.RESET}", data["isp"])
    print(f"{Fore.GREEN}[+] RegionName:{Fore.RESET}", data["regionName"])
    print(f"{Fore.GREEN}[+] Query:{Fore.RESET}", data["query"])
    print()
    print(f"{shr6h} {Fore.RESET}FINISHED")
    time.sleep(6)
    menu()    
    
def dmain():
    os.system('cls')
    os.system(f'title Matrix - Domain Scanner - Theme: {theme}')
    print(faded_text)
    print()
    domain = input(f"{shr6h} {Fore.RESET}Enter the Domin to scan: ")
    print()
    print()
    subdomains = ["www", "build", "web", "dev", "staff", "mc", "play", "sys", "node1", "node2", "node3", "builder", "developer", "test", "test1", "forum", "bans", "baneos", "ts", "ts3", "sys1", "sys2", "mods", "bungee", "bungeecord", "array", "spawn", "server", "help", "client", "api", "smtp", "s1", "s2", "s3", "s4", "server1", "server2", "jugar", "login", "mysql", "phpmyadmin", "demo", "na", "eu", "us", "es", "fr", "it", "ru", "support", "developing", "discord", "backup", "buy", "buycraft", "go", "dedicado1", "dedi", "dedi1", "dedi2", "dedi3", "minecraft", "prueba", "pruebas", "ping", "register", "cdn", "stats", "store", "serie", "buildteam", "info", "host", "jogar", "proxy", "vps", "ovh", "partner", "partners", "appeals", "appeal", "store-assets", "admin", "panel", "discord", "KSA", "status" ,"Protection", "system", "Both", "Admins", "file", "files", "code", "developer", "development", "storee", "net", "999", "666", "gift", "payment"]
    for subdomain in subdomains:
        try:
            fullsub = str(subdomain)+"."+str(domain)
            ipofsub = socket.gethostbyname(str(fullsub))
            print(Fore.BLUE + "[ Matrix ] " + fullsub + " » " + ipofsub)
        except:
            pass
    
    print()
    print(f"{shr6h} {Fore.RESET}FINISHED")
    time.sleep(6)
    menu()

def ipconfig():
    os.system('cls')
    os.system(f'title Matrix Protection - System Scans - Theme: {theme}')
    print(faded_text)
    print(Fore.LIGHTBLUE_EX)
    os.system(f'sfc /scannow')
    time.sleep(3)
    menu()

def stat():
    os.system('cls')
    os.system(f'title Matrix Protection - Stat My Net - Theme: {theme}')
    print(faded_text)
    print(Fore.LIGHTBLUE_EX)
    print("Wait for the information to be collected")
    time.sleep(2)
    os.system(f'netstat')
    time.sleep(5)
    menu()


def sens():
    os.system('cls')
    os.system(f'title Matrix Protection - System Scans - Theme: {theme}')
    print(faded_text)
    print(Fore.LIGHTBLUE_EX)
    os.system(f'DISM /Online /Cleanup-Image /RestoreHealth')
    time.sleep(3)
    menu()

def fix():
    os.system('cls')
    os.system(f'title Matrix - System Scans - Theme: {theme}')
    print(faded_text)
    print(Fore.LIGHTBLUE_EX)
    os.system(f'ipconfig /flushdns')
    time.sleep(3)
    menu()


def temp():
    os.system('cls')
    os.system(f'title Matrix - System Scans - Theme: {theme}')
    print(faded_text)
    print(Fore.LIGHTBLUE_EX)
    os.system(f'del /q/f/s temp *')
    os.system(f'taskkill/im discord.exe')
    time.sleep(3)
    menu()


  
def menu():
    os.system('cls')
    os.system(f'title Matrix - Main - Theme: {theme}')
    print(faded_text)
    print()
    print(f'''
                 
{Fore.RESET}({number1}{Fore.RESET}) Port Scanner
{Fore.RESET}({number2}{Fore.RESET}) Domain Scanner
{Fore.RESET}({number3}{Fore.RESET}) IP Pinger
{Fore.RESET}({number4}{Fore.RESET}) Domain & IP Info
''')


    print()
    choice = input(f"{chose}Matrix @~ {Fore.RESET}")
    choice = int(choice)
    if choice == 1:
        portsc()
    elif choice == 2:
        dmain()
    elif choice == 3:
        pinger()
    elif choice == 4:
        info()
menu()