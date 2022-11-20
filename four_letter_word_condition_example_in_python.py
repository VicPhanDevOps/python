#!/bin/python

# check four letter word in Python

import colorama, os, sys, traceback
from colorama import Fore, Style
from datetime import datetime
colorama.init()


def checkOs(): 
    print("Started checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))

    if sys.platform == "win32": 
        print(Fore.GREEN + "Operating System:", end="")
        os.system('ver')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Windows"

    elif sys.platform == "darwin": 
        print(Fore.GREEN + "Operating System:")
        os.system('sw_vers')
        print(Style.RESET_ALL, end="")
        operatingSystem = "macOS"

    elif sys.platform == "linux": 
        print(Fore.GREEN + "Operating System: ")
        os.system('uname -r')
        print(Style.RESET_ALL, end="")
        operatingSystem = "Linux"

    print("Finished checking operating system at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    print("")
    return operatingSystem


def getFourLetterWord(operatingSystem): 
    if operatingSystem == "Window": 
        fourLetterWord = str(input("Please type a four-letter word and press the \"Enter\" key (Example: code): "))

        print("")

    else: 
        fourLetterWord = str(input("Please type a four-letter word and press the \"return\" key (Example: code): "))

        print("")
        
    return fourLetterWord


def checkParameters(fourLetterWord): 
    print("Started checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
    valid = "true"

    print("Parameters:")
    print("-----------------------------------------")
    print("fourLetteWord: {0}".format(fourLetterWord))
    print("-----------------------------------------")

    if fourLetterWord == None: 
        print(Fore.RED + "fourLetterWord is not set." + Style.RESET_ALL)
        valid = "false"

    if valid == "true": 
        print(Fore.GREEN + "All parameters checks passed." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        print("")

    else: 
        print(Fore.RED + "One or more parameters are incorrect." + Style.RESET_ALL)

        print("Finished checking parameters at", datetime.now().strftime("%Y-%m-%d %H:%M %p"))
        exit("")


def checkFourLetterWord():
    print("\nLet's check a four letter word in Python!\n")
    operatingSystem = checkOs()

    if len(sys.argv) > 2: 
        fourLetterWord = str(sys.argv[1])

    else: 
        fourLetterWord = getFourLetterWord(operatingSystem)

    checkParameters(fourLetterWord)

    try: 
        startDateTime = datetime.now()
        print("Started checking four letter word at", startDateTime.strftime("%Y-%m-%d %H:%M %p"))

        wordLength = len(fourLetterWord)

        if wordLength == 4:
            print(Fore.GREEN + "{0} is a four letter world.  Well done!".format(fourLetterWord))
            print("" + Style.RESET_ALL)
        else:
            print(Fore.RED + "Sorry but {0} is not a four letter word.".format(fourLetterWord))
            print("" + Style.RESET_ALL)

        print(Fore.GREEN + "Successfully checked four letter word." + Style.RESET_ALL)

        finishedDateTime = datetime.now()
        print("Finished checking four letter word at", finishedDateTime.strftime("%Y-%m-%d %H:%M %p"))

        duration = finishedDateTime - startDateTime
        print("Total execution time: {0} second(s)".format(duration.seconds))
        print("")

    except Exception as e: 
        print(Fore.RED + "Failed to check four letter word")
        print(e)
        print(traceback.print_stack)
        exit("" + Style.RESET_ALL)


checkFourLetterWord()
