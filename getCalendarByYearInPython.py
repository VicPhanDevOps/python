#!/bin/python

# get calendar by year in Python

# you can run this script with: python3 getCalendarByYearInPython.py < year >

import calendar, colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs():
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System: ")
        os.system('ver')
        print(Style.RESET_ALL)
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System: ")
        os.system('sw_vers')
        print(Style.RESET_ALL)
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System: ")
        os.system('uname -r')
        print(Style.RESET_ALL)
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    print("")
    return operatingSystem


def getYear(operatingSystem): 
    if operatingSystem == "Windows":
        year = int(input("Please type the year you want a calendar for and press \"Enter\" key (Example: 1999): "))

        print("")
        
    elif operatingSystem == "macOS" or operatingSystem == "Linux": 
        year = int(input("Please type the year you want a calendar for and press \"return\" key (Example: 1999): "))

        print("")
    
    return year


def checkParameters(year): 
    print("Started checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    
    valid = "true"

    print("Parameters:")
    print("----------------------")
    print("year: {0}".format(year))
    print("----------------------")

    if year == None: 
        print(Fore.RED + "year is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true": 
        print(Fore.GREEN + "All parameter checks passed." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%y-%m-%d %H:%M %p"))

        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%y-%m-%d %H:%M %p"))

        exit("")


def getCalendarByYear(): 
    print("\Let's get a calendar by year in Python!\n")
    operatingSystem = checkOs()

    if len(sys.argv) >= 2: 
        year = int(sys.argv[1])

    else: 
        year = getYear(operatingSystem)

    checkParameters(year)

    try: 
        startDateTime = datetime.now()

        print("Started getting calendar by year at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        print("")
        calendar.prcal(year)
        print("")
        
        print(Fore.GREEN + "Successfully got calendar by year" + Style.RESET_ALL)

        finishedDateTime = datetime.now()

        print("Finished getting calendar by year at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")
        
    except Exception as e: 
        print(Fore.RED + "Failed to get calendar by year.")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


getCalendarByYear()
