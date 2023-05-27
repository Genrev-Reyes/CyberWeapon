import os
from time import sleep
import sys







def package():
    os.system("apt install wget")


logo="""
  ____      _                    _   _   _             _
 / ___|   _| |__   ___ _ __     / \ | |_| |_ __ _  ___| | __
| |  | | | | '_ \ / _ \ '__|   / _ \| __| __/ _` |/ __| |/ /
| |__| |_| | |_) |  __/ |     / ___ \ |_| || (_| | (__|   <
 \____\__, |_.__/ \___|_|    /_/   \_\__|\__\__,_|\___|_|\_\
                  |___/

                            [GenrevReyes]


"""





def clear():
    sleep(1)
    os.system("clear")

sleep(2)

help="""
--------------------           -----------------------
Commands                        Discription

[#] show tools                  To see the tools

[#] install                     Tool Number

[#] show more                   To see other tools

[#] clear                       To clear the terminal

[#] exit                        Exit

"""


show_tools = """

_________________________________
|                               |
|All This Tool Are Working 100% |
|_______________________________|


[COMMANDS]


[1] MaxPhisher

[2] Ghost

[3] Little Brother

[4] RouterSploit

[5] Nethunter

[6] PhoneInfoga

[7] SocialBox

[8] Metasploit Framework

[9] Cam-Hackers

[10] Wifite


"""


show_more="""

[11] Zphisher

[12] SMS

[13] T_bomb

[14] Sherlock

[15] AndroRAT
"""




def MaxPhisher():
    os.system("git clone https://github.com/KasRoudra/MaxPhisher")
    print(f"[✓]MaxPhisher Succesfully Installed")
    clear()
    print(logo)


def Ghost():
    os.system("git clone https://github.com/FazalMahmood/ghost.git")
    print(f'[✓]Ghost Succesfully Installed')
    clear()
    print(logo)
package()

def LittleBrother():
    os.system("git clone https://github.com/Lulz3xploit/LittleBrother")
    print(f'[✓]LittleBrother Installed Succesfully')
    clear()
    print(logo)
def RouterSploit():
    os.system("git clone https://www.github.com/threat9/routersploit")
    print("[✓]RouterSploit Installed Succesfully")
    clear()
    print(logo)

def Nethunter():
    os.system("wget -O nethunter https://offs.ec/2MceZWr")
    os.system("chmod +x nethunter ")
    print("[✓]Nethunter Installed Succesfully")
    clear()
    print(logo)


def SocialBox():
    os.system("git clone https://github.com/TunisianEagles/SocialBox.git")
    print("[✓]SocialBox Installed Succesfully")
    clear()
    print(logo)


def Metasploit():
    os.system("wget https://github.com/gushmazuko/metasploit_in_termux/raw/master/metasploit.sh")
    os.system("chmod +x metasploit.sh")
    print("[✓]Metasploit Framework Succesfully Installed")
    clear()
    print(logo)

def PhoneInfoga():
   os.system("git clone https://github.com/sundowndev/PhoneInfoga")
   print("[✓]PhoneInfoga Installed Succesfully")
   clear()
   print(logo)


def Cam_Hackers():
    os.system("git clone https://github.com/AngelSecurityTeam/Cam-Hackers")
    print("[✓]Cam-Hackers Installed Succesfully")
print(logo)



def Wifite():
    os.system("git clone https://github.com/derv82/wifite2.git")
    print("[✓]Wifite Installed Succesfully")
    clear()
    print(logo)




def Zphisher():
    os.system("git clone https://github.com/htr-tech/zphisher")
    print("[✓]Zphisher Installed Succesfully")
    clear()
    print(logo)


def sms():
    os.system("git clone https://github.com/rixon-cochi/SMF.git")
    print("[✓]SMS Installed Succesfully")
    clear()
    print(logo)

def T_bomb():
    os.system("git clone https://github.com/TheSpeedX/TBomb.git")
    os.system("pip3 install tbomb")
    print("[✓]T_bomb Installed Succesfully")
    clear()
    print(logo)



def Sherlock():
    os.system(" git clone https://github.com/sherlock-project/sherlock.git")
    clear()
    print(logo)

def AndroRAT():
    os.system("git clone https://github.com/karma9874/AndroRAT.git")
    print("[✓]AndroRAT Installed Succesfully")
    clear()
    print(logo)





def install():
    choice = input("Enter Tool Number: ")
    if (choice) == "1":
        sleep(1)
        MaxPhisher()

    if (choice) == "2":
        sleep(1)
        Ghost()
    if (choice) == "3":
        sleep(1)
        LittleBrother()
    if (choice) == "4":
        sleep(1)
        RouterSploit()
    if (choice) == "5":
        sleep(1)
        Nethunter()
    if (choice) == "6":
        sleep(1)
        PhoneInfoga()
    if (choice) == "7":
        sleep(1)
        SocialBox()
    if (choice) == "8":
        sleep(1)
        Metasploit()
    if (choice) == "9":
        sleep(1)
        Cam_Hackers()
    if (choice) == "10":
        sleep(1)
        Wifite()
    if (choice) == "11":
        Zphisher()
    if (choice) == "12":
        sms()
    if (choice) == "13":
        T_bomb()
    if (choice) == "14":
        Sherlock()
    if (choice) == "15":
        AndroRAT()

    if not choice in ('1', '2', '3', '4', '5', '6','7', '8', '9','10', '11', '12', '13', '14', '15'):
        sleep(1)

        print("[!]Wrong input")






host_name = input("Enter username: ")
def console():
    while True:
        user = input(f"{host_name}~# ")
        if (user) == "help":
            print(help)
        if (user) == "exit":
            sys.exit()
        if (user) == "show tools":
            print(show_tools)
        if (user) == "clear":
            clear()
            print(logo)
        if (user) == "install":
            sleep(1)
            install()
        if (user) == "show more":
            print(show_more)



run = console()