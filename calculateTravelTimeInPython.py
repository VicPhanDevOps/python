#!/bin/python

# calculate travel time

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()

def checkOs():
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

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

    print("Finished checking operating system at ", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    print("")
    return operatingSystem

def getRate(operatingSystem):
    if operatingSystem == "Windows": 
        rate = float(input("Please type the rate (miles per hour) and press \"Enter\" key (Example: 45): "))

        print("")
    elif operatingSystem == "macOS" or operatingSystem == "Linux": 
        rate = float(input("Please type the rate (miles per hour) and press \"return\" key (Example: 45): "))

        print("")
    return rate 

def getDistance(operatingSystem):
    if operatingSystem == "Windows": 
        distance = float(input("Please type the distance (miles) and press \"Enter\" key (Example: 100): "))
    elif operatingSystem == "macOS" or operatingSystem == "Linux": 
        distance = float(input("Please type the distance (miles) and press \"return\" key (Example: 100): "))

    print("")
    return distance

def checkParameters(rate, distance): 
    print("Started checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    valid = "true"

    print("Parameters:")
    print("------------------------------")
    print("rate    : {0}".format(rate))
    print("distance: {0}".format(distance))
    print("------------------------------")

    if rate == None: 
        print(Fore.RED + "rate is not set." + Style.RESET_ALL)
        valid = "false"

    if distance == None: 
        print(Fore.RED + "distance is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true": 
        print(Fore.GREEN + "All parameter checks passed." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        print("")
    else: 
        print(Fore.RED + "One or more parameter checks are incorrect." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

        exit("")

def calculateTravelTime(): 
    print("\nCalculate travel time in Python!\n")
    operatingSystem = checkOs()

    if len(sys.argv) > 2: 
        rate     = float(sys.argv[1])
        distance = float(sys.argv[2])
    else: 
        rate = getRate(operatingSystem)
        distance = getDistance(operatingSystem)

    checkParameters(rate, distance)

    try: 
        startDateTime = datetime.now()
        
        print("Started calculating travel time at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        print(Fore.YELLOW + "Travel time: {0} hours ".format(distance / rate))
        print(Fore.GREEN + "Successfully calcuated travel time." + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished calculating travel time at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p")) 

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} seconds".format(duration.seconds))
        print("")
    except Exception as e:
        print(Fore.RED + "Failed to calculate travel time" + Style.RESET_ALL)
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)

calculateTravelTime()