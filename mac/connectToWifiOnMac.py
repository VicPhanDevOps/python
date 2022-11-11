#!/bin/python

# connect to Wi-Fi on Mac

# you can run this script with: python3 connectToWifiOnMac.py < SSID > < password >

import colorama, getpass, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOsForMac():
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        
        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")
    else: 
        print(Fore.RED + "Sorry but this script only runs on Mac." + Style.RESET_ALL)

        print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        exit("")


def getWifiSsid(): 
    wifiSsid = str(input("Please type the SSID of the Wi-Fi network you wish to connect to and press \"return\" key (Example: Starbucks): "))

    print("")
    return wifiSsid


def getWifiPassword(): 
    wifiPassword = getpass.getpass("Please type the password for the Wi-Fi network you wish to connect to and press \"return\" key (Example: Password123): ")

    print("")
    return wifiPassword


def checkParameters(wifiSsid, wifiPassword): 
    print("Started checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    valid = "true"

    print("Parameters:")
    print("--------------------------------------")
    print("wifiSsid    : {0}".format(wifiSsid))
    print("wifiPassword: {0}".format("***"))
    print("--------------------------------------")

    if wifiSsid == None: 
        print(Fore.RED + "wifiSsid is not set." + Style.RESET_ALL)
        valid = "false"

    if wifiPassword == None:
        print(Fore.RED + "wifiPassword is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true":
        print(Fore.GREEN + "All parameter checks password." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect.", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        exit("")


def connectToWifi(): 
    print("Connect to Wi-Fi on Mac.\n")
    checkOsForMac()

    if len(sys.argv) > 2:
        wifiSsid     = str(sys.argv[1])
        wifiPassword = str(sys.argv[2])

    else: 
        wifiSsid     = getWifiSsid()
        wifiPassword = getWifiPassword()

    checkParameters(wifiSsid, wifiPassword)

    try: 
        startDateTime = datetime.now()

        print("Started connecting to WiFi at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))
        
        connectToWifi = 'networksetup -setairportnetwork en0 {0} {1}'.format(wifiSsid, wifiPassword)

        os.system(connectToWifi)

        print(Fore.GREEN + "Successfully connected to WiFi." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished connecting to WiFi at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        print("")
        
    except Exception as e: 
        print(Fore.RED + "Failed to connect to WiFi.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)
    
        
connectToWifi()