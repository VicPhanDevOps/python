#!/bin/python

# check Node in Python 

import colorama, os, sys, subprocess, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()

def checkOs():
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('ver'))
        print(Style.RESET_ALL)
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('sw_vers'))
        print(Style.RESET_ALL)
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System: ")
        print(os.system('uname -r'))
        print(Style.RESET_ALL)
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    print("")
    return operatingSystem

def checkNode(): 
    print("\nCheck Node in Python.\n")
    operatingSystem = checkOs()

    try:
        startDateTime = datetime.now()
        
        print("Started checking Node at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        FNULL = open(os.devnull,'w')

        if operatingSystem == "macOS" or operatingSystem == "Linux":

            checkNodeOnMacOrLinux = subprocess.call(['which', 'node'], stdout=FNULL) 

            if checkNodeOnMacOrLinux == 0:
                print(Fore.GREEN + "Node is installed."+ Style.RESET_ALL)
                os.system('node --version')
                print(Fore.GREEN + "Successfully checked Node." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Node at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "Node is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking Node at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")

        elif operatingSystem == "Windows": 
            
            checkNodeOnWindows = subprocess.call(['where', 'node'], stdout=FNULL)

            if checkNodeOnWindows == 0:
                print(Fore.GREEN + "Node is installed."+ Style.RESET_ALL)
                os.system('node --version')
                print(Fore.GREEN + "Successfully checked Node." + Style.RESET_ALL)

                finishedDateTime = datetime.now()

                print("Finished checking Node at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                print("")

            else: 
                print(Fore.RED + "Node is not installed." + Style.RESET_ALL)
                
                finishedDateTime = datetime.now()

                print("Finished checking Node at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

                duration = finishedDateTime - startDateTime
                print("Total execution time: {0} second(s)".format(duration.seconds))
                exit("")
                
    except Exception as e: 
        print(Fore.RED + "Failed to check Node in Python.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)

checkNode()