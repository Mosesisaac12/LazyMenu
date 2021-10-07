"""
Commons Clause - License Condition v1.0
Copyright Que 2021
The Software is provided to you by the Licensor under the
License, as defined below, subject to the following condition.
Without limiting other conditions in the License, the grant
of rights under the License will not include, and the License
does not grant to you, the right to Sell the Software.
For purposes of the foregoing, “Sell” means practicing any or
all of the rights granted to you under the License to provide
to third parties, for a fee or other consideration (including
without limitation fees for hosting or consulting/ support
services related to the Software), a product or service whose
value derives, entirely or substantially, from the functionality
of the Software. Any license notice or attribution required by
the License must also include this Commons Clause License
Condition notice.
All Rights Reserved. You are not allowed to redistribute this software, or use
the software to build derivative works based upon without prior written permission.
This software is open-source only for Educational Purposes, if you learn\copy-over\edit anything from LazyMenu you must give appropriate credit,
provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner.


Software: LAZYMENU
"""
# https://discord.gg/xysmj9mHxV

import webbrowser
import colorama
from colorama import Fore, Back, Style
import requests, os, threading, sys, time, random, ctypes, webbrowser,re, hashlib, datetime, os.path
colorama.init(autoreset=True)
from datetime import date
from time import sleep
os.system('cls' if os.name == 'nt' else 'clear')
os.system("| LazyMenu | Version = BETA | Made by cutieQue (https://github.com/cutieQue)")
def menu():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{Fore.LIGHTRED_EX}
                ██╗░░░░░░█████╗░███████╗██╗░░░██╗███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗██╗
                ██║░░░░░██╔══██╗╚════██║╚██╗░██╔╝████╗░████║██╔════╝████╗░██║██║░░░██║██║
                ██║░░░░░███████║░░███╔═╝░╚████╔╝░██╔████╔██║█████╗░░██╔██╗██║██║░░░██║██║
                ██║░░░░░██╔══██║██╔══╝░░░░╚██╔╝░░██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║╚═╝
                ███████╗██║░░██║███████╗░░░██║░░░██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝██╗
                ╚══════╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░╚═╝
    """)
    print("")

    print(f"{Fore.LIGHTYELLOW_EX}[1] - Tools         [2] - Join Discord Server / Support        [3] - Free Games / Software\n\n")
    print(f"{Fore.LIGHTYELLOW_EX}[98] - Exit")
menu()

option = int(input(f"{Fore.LIGHTRED_EX}\n[>] {Fore.RESET}"))

def tools():
    print("[TEST] LazyTools Test")

while option !=1:
    if option == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        tools()
    elif option == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        sleep(1)
        print(f"{Fore.LIGHTGREEN_EX}Redirecting You To DevSec Discord Server!")
        sleep(4)
        webbrowser.open_new('https://discord.gg/xysmj9mHxV')
    elif option == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        sleep(0.5)
        print(f"{Fore.RED}COMMAND NOT AVAILABLE ON BETA!\nPlease Check for a New {Fore.LIGHTCYAN_EX}Version!")
        sleep(3.52)
    elif option == 98:
        sleep(1)
        print(f"{Fore.LIGHTCYAN_EX} [!] {Fore.RESET}| {Fore.RED}Exiting...")
        sleep(0.92)
        exit()
    else:
        print(f"{Fore.RED}Invalid option!")
        sleep(2)
    menu()
    option = int(input(f"{Fore.LIGHTRED_EX}\n[>] {Fore.RESET}"))

def tool_menu():
    sleep(0.67)
    os.system('cls' if os.name == 'nt' else 'clear')
    print(f"""{Fore.LIGHTRED_EX}        
                    ██╗░░░░░░█████╗░███████╗██╗░░░██╗████████╗░█████╗░░█████╗░██╗░░░░░░██████╗██╗
                    ██║░░░░░██╔══██╗╚════██║╚██╗░██╔╝╚══██╔══╝██╔══██╗██╔══██╗██║░░░░░██╔════╝██║
                    ██║░░░░░███████║░░███╔═╝░╚████╔╝░░░░██║░░░██║░░██║██║░░██║██║░░░░░╚█████╗░██║
                    ██║░░░░░██╔══██║██╔══╝░░░░╚██╔╝░░░░░██║░░░██║░░██║██║░░██║██║░░░░░░╚═══██╗╚═╝
                    ███████╗██║░░██║███████╗░░░██║░░░░░░██║░░░╚█████╔╝╚█████╔╝███████╗██████╔╝██╗
                    ╚══════╝╚═╝░░╚═╝╚══════╝░░░╚═╝░░░░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝╚═════╝░╚═╝
                                    {Fore.LIGHTYELLOW_EX}If Any of these r your tools, 
                                    join our server & tell us & we will credit you
                                                                                """)
    print(f"""{Fore.LIGHTYELLOW_EX}
            [1] - Discord Server Lookup                         [7] - Discord Console Hacks
            [2] - ODiscord (Bundle of Discord Tools)            
            [3] - Discord Webhook Spammer
            [4] - Discord Nitro Generator
            [5] - LazyLeech
            [6] - Discord Token Info

            [98] - Exit
    """)
tool_menu()

option1 = int(input(f"{Fore.LIGHTRED_EX}\n[>] {Fore.RESET}"))

while option1 !=0:
    if option1 == 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.LIGHTCYAN_EX} [!] {Fore.RESET}| {Fore.LIGHTRED_EX}Redirecting You to: {Fore.RESET}cutieQue/Discord-Server-Lookup")
        sleep(4)
        webbrowser.open_new('https://github.com/cutieQue/Discord-Server-Lookup')
    elif option1 == 2:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.LIGHTCYAN_EX} [!] {Fore.RESET}| {Fore.LIGHTRED_EX}Redirecting to: {Fore.RESET}I2rys/ODiscord...")
        sleep(4)
        webbrowser.open_new('https://github.com/I2rys/ODiscord')
        sleep(0.6)
        menu()
    elif option1 == 3:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.LIGHTCYAN_EX} [!] {Fore.RESET}| {Fore.LIGHTRED_EX}Redirecting to: {Fore.RESET}cutieQue/WebhookSpammer...")
        sleep(4)
        webbrowser.open_new('https://github.com/cutieQue/WebhookSpammer')
        sleep(0.6)
        menu()
    elif option1 == 4:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.LIGHTCYAN_EX} [!] {Fore.RESET}| {Fore.LIGHTRED_EX}Redirecting to: {Fore.RESET}cutieQue/Discord-Nitro-Generator-Checker...")
        sleep(4)
        webbrowser.open_new('https://github.com/cutieQue/Discord-Nitro-Generator-Checker')
        sleep(0.6)
        menu()
    elif option1 == 5:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.LIGHTCYAN_EX} [!] {Fore.RESET}| {Fore.LIGHTRED_EX}Redirecting to: {Fore.RESET}MoonS3c/LazyLeech...")
        sleep(4)
        webbrowser.open_new('https://github.com/MoonS3c/LazyLeech')
        sleep(0.6)
        menu()       
    elif option1 == 6:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.LIGHTCYAN_EX} [!] {Fore.RESET}| {Fore.LIGHTRED_EX}Redirecting to: {Fore.RESET}I2rys/DTSpider...")
        sleep(4)
        webbrowser.open_new('https://github.com/I2rys/DTSpider')
        sleep(0.6)
        menu()     
    elif option1 == 7:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"{Fore.LIGHTCYAN_EX} [!] {Fore.RESET}| {Fore.LIGHTRED_EX}Redirecting to: {Fore.RESET}cutieQue/Console-Hacks...")
        sleep(4)
        webbrowser.open_new('https://github.com/cutieQue/Console-Hacks')
        sleep(0.6)
        menu() 
    elif option1 == 98:
        print(f"{Fore.LIGHTCYAN_EX} [!] {Fore.RESET}| {Fore.RED}Exiting...")
        sleep(2)
        exit()
    else:
        print(f"{Fore.RED}Invalid option please either pick one of the numbers below!")
    tool_menu()
    option1 = int(input(f"{Fore.LIGHTRED_EX}\n[>] {Fore.RESET}"))




