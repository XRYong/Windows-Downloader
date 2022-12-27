from os import startfile, system
from os.path import isfile
from sys import exit
from time import sleep
from timeit import default_timer
from urllib.request import urlretrieve
from webbrowser import open as webopen
from platform import release

try:
  from colorama import *
  from ping3 import ping
  from psutil import cpu_count, cpu_percent, disk_usage, virtual_memory
  from XeLib import cls, printer, download, color, getmyping
  from XTLLib import fwrite, runaspowershell, SetVars
except:
  system("pip install colorama ping3 psutil XeLib XTLLib")

start = default_timer





def runqol(froms, choose):
    # If the user inputs "99", exit the program.
    if choose == "99": 
        exit()

    else: 
        # Otherwise, print an error message and sleep for 3 seconds.
        print("No option named " + choose)
        sleep(3)

def achooser(choose, option):
    if option == choose or option.upper() == choose or option.capitalize() == choose or option.title() == choose or option.lower() == choose: return True

def cles():
  system("cls")

def dl(org, url, urlr, name):
    # Try and except so the program won't crash when the website isn't accesible
    try:
        if isfile(urlr) == True:
            print("ERROR 1 - File " + urlr + " already exists!")
            chose = input(Fore.RED+"[S>] Overwrite?"+Fore.RESET+" ("+Fore.GREEN+"Y"+Fore.RESET+"/"+Fore.RED+"n"+Fore.RESET+"): ")
            if chose == "Y" or chose == "y": pass
            elif chose == "N" or chose == "n":
                if org == 1: p1()
            else: runqol(0, chose)
    except:
        print("ERROR 2: Can't check for file overwrite. Missing file premissions?"); sleep(6)
    # Download module is located here.
    try:
        download(url, urlr, name)
        if name != "WindowsOnReins":
            startfile(urlr)
        if org == 1: p1()
        # Only `if` statements will work with this
    except:
      print("ERROR 3: Can't download file from the server...") ; sleep(3)

def p1():
  while True:
    cles()
    print(" ┌─────────────────────────────────────────────────────┐\n",
          "| Made by  X.R. Yong   [W]  Windows                   |\n",
          "| 1. Windows 11    [x64]                              |\n",
          "| 2. Windows 10    [x64 x32]                          |\n",
          "| 3. Windows 8.1   [x64]                              |\n",
          "| 4. Windows 8     [x64]                              |\n",
          "| 5. Windows 7     [x64]                              |\n",
          "| 6. Windows 8.1   [x32]                              |\n",
          "| 7. Windows 8     [x32]                              |\n",
          "| 8. Windows 7     [x32]                              |\n",
          "| 9. Windows Vista [x64]                              |\n",
          "|10. Windows Vista [x32]                              |\n",
          "|11. Windows XP    [x64]                              |\n",
          "|12. Windows XP    [x32]                              |\n",
          "|                                                     |\n",
          "| Example: [W1]                              99 - Exit|\n",
          "└─────────────────────────────────────────────────────┘\n")
    choose = input(" > ")
    if achooser(choose, "W1"):  webopen("https://www.microsoft.com/software-download/windows11/")
    elif achooser(choose, "W2"): webopen("https://www.microsoft.com/en-us/software-download/windows10")
    elif achooser(choose, "W3"): webopen("https://dl.malwarewatch.org/windows/Windows%208.1%20%28x64%29.iso")
    elif achooser(choose, "W4"): webopen("https://dl.malwarewatch.org/windows/Windows%208%20%28x64%29.iso")
    elif achooser(choose, "W5"): webopen("https://dl.malwarewatch.org/windows/Windows%207%20%28x64%29.iso")
    elif achooser(choose, "W6"): webopen("https://dl.malwarewatch.org/windows/Windows%208.1.iso")
    elif achooser(choose, "W7"): webopen("https://dl.malwarewatch.org/windows/Windows%208.iso")
    elif achooser(choose, "W8"): webopen("https://dl.malwarewatch.org/windows/Windows%207.iso")
    elif achooser(choose, "W9"): webopen("https://dl.malwarewatch.org/windows/Windows%20Vista%20%28x64%29.iso")
    elif achooser(choose, "W10"): webopen("https://dl.malwarewatch.org/windows/Windows%20Vista.iso")
    elif achooser(choose, "W11"): webopen("https://dl.malwarewatch.org/windows/Windows%20XP%20%28x64%29.iso")
    elif achooser(choose, "W12"): webopen("https://dl.malwarewatch.org/windows/Windows%20XP.iso")

    
    else: runqol(1, choose)

def eula():
  cles()

  z = True
  while z == True:
    print("Responsible for your own action...\n",
    "I am not responsible.")

    agree = input("Do you agree? Y/n: ")

    if achooser(agree, "y"):
            print("You agreed to the EULA.")
            z = False
        
        # If the user does not agree, exit the program
    elif achooser(agree, "n"):
      print("Ok, come back if you change your mind."); exit(sleep(3))
        
        # If the user's input is not "y" or "n", call the runqol() function
    else: runqol(0, agree)
    
    # Delete the variable z
  del z



eula()
p1()

