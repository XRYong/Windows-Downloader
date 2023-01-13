## Changelog
## Fixed after downloading file won't start automaticaly

from os import startfile, system
from os.path import isfile
from sys import exit
from time import sleep
from timeit import default_timer
from urllib.request import urlretrieve
from webbrowser import open as webopen
from platform import release
from concurrent.futures import ThreadPoolExecutor
from contextlib import closing
from os.path import isfile
from os import system
from os import startfile
from time import perf_counter
from urllib.parse import urlparse
from platform import system as platform


start = default_timer

## pip modules

try:
    print("Loading Modules...")
    from colorama import Fore, init
    from tqdm import tqdm
    from requests import Session
    from requests.adapters import HTTPAdapter
    from ping3 import ping
    from lastversion import latest
    import wmi
    from tkinter import ttk
    from tkinter import Tk
    import tkinter
    from tkinter import Button, Label
except:
    print("Downloading Modules...")
    system("pip install -U colorama tqdm requests ping3 lastversion wmi tkinter")

init(autoreset=True)

class com():
    def ping():
        if ping("github.com") == None or False:
            print("com.error No Internet")

class bootodr():
    def noint_odr():
        print("No Internet Boot Order")
        printer.sys("Starting...")
        eula()
        p1()
    def devmd_odr():
        print("Devoloper Mode Enabled...")
        printer.sys("Starting...")
        p1()
    def fast_odr():
        print("Fast Start...")
        printer.sys("Starting...")
        printer.sys("Running Network Check...")
        prep()
        p1()
class cmd():
    def console():
        z = True
        hp = "help"
        tl = "t.list"
        tlk = "t.kill"
        st = "t.start"
        tr = "t.restart"
        gt = "github"
        while z == True:
            print(f"Windows Utility V{version}")
            cns_in = input("COMMAND PROMPT >")
            if cns_in == "E" or cns_in == "e" or cns_in == "99": del z ; exit()
            else: cls() ; print(f"COMMAND PROMPT >{cns_in}") ; system(cns_in)
            if cns_in == "ls" or cns_in == "LS" or cns_in == "lS" or cns_in == "lS":
                cls()
                print(f"Windows Utility V{version}")
                print(f"COMMAND PROMPT >{cns_in}")
                system("dir /s")
            if cns_in == "dl" or cns_in == "DL" or cns_in == "dL" or cns_in == "Dl":
                cls()
                print(f"Windows Utility V{version}")
                print(f"COMMAND PROMPT >{cns_in}")
                dol = input("URL >")
                savas = input("Save As >")
                download(dol, savas, savas)
            elif hp == cns_in or hp.upper == cns_in or hp.capitalize == cns_in or hp.lower == cns_in or hp.title == cns_in:
                cls()
                print(f"Windows Utility V{version}")
                print(f"COMMAND PROMPT >{cns_in}")
                print("https://github.com/XRYong/Windows-Utility/wiki/Commands")
                print("Custom Windows Utility Commands:")
                print("ls -------- List Files In A Directory.")
                print("dl -------- Download A File From A URL And Save The File.")
                print("e --------- Exit")
                print("t.kill ---- Kill A Program, Just Type t.kill It Will Ask For Process.")
                print("t.start --- Start A Program, Just Type t.start It Will Ask For Process.")
                print("t.restart - Restart A Program, Just Type t.restart It Will Ask For Process.")
                print("github ---- Windows Utility Github Page")
            elif tl == cns_in or tl.upper == cns_in or tl.capitalize == cns_in or tl.lower == cns_in or tl.title == cns_in:
                cls()
                print(f"Windows Utility V{version}")
                print(f"COMMAND PROMPT >{cns_in}")
                f = wmi.WMI()
                for process in f.Win32_Process():
     
                    # Displaying the P_ID and P_Name of the process
                    print(f"{process.ProcessId:<10} {process.Name}")
            elif tlk == cns_in or tlk.upper == cns_in or tlk.capitalize == cns_in or tlk.lower == cns_in or tlk.title == cns_in:
                cls()
                pr = input("PROCESS >")
                system(f"TASKKILL /f /im {pr}")
            elif st == cns_in or st.upper == cns_in or st.capitalize == cns_in or st.lower == cns_in or st.title == cns_in:
                cls()
                pr = input("PROCESS >")
                system(f"START {pr}")
            elif tr == cns_in or tr.upper == cns_in or tr.capitalize == cns_in or tr.lower == cns_in or tr.title == cns_in:
                cls()
                pr = input("PROCESS >")
                system(f"TASKKILL /f /im {pr}")
                system(f"START {pr}")
            elif gt == cns_in or gt.upper == cns_in or gt.capitalize == cns_in or gt.lower == cns_in or gt.title == cns_in:
                cls()
                print("Project Windows Utility.")
                print("https://github.com/XRYong/Windows-Utility")
            elif cns_in == "~": z = False ; del z ; p1()

    def uicmdcs():
        print("OneUI (V1.1)")
        winr = tkinter.Tk()
        def nors():
            winr.destroy()
            ns()
        def norcmd():
            winr.destroy()
            cmd.console()
        def fastst():
            winr.destroy()
            bootodr.fast_odr()
        winr.geometry("500x500")
        winr.title("OneUI (V1.1)")
        l1l = Label(winr, text="OneUI (V1.1)")
        l1l.pack()
        b1cmd = Button(winr, text="Command Prompt", padx=10, pady=10, command = norcmd)
        b1cmd.pack()
        b1p1 = Button(winr, text="Normal Start", padx=10, pady=10, command=nors)
        b1p1.pack()
        b2p1 = Button(winr, text="Fast Start", padx=10, pady=10, command=fastst)
        b2p1.pack()
        winr.mainloop()

class printer():
    def red(text):
        print(Fore.RED + text + Fore.RESET)
    def yellow(text):
        print(Fore.YELLOW + text + Fore.RESET)
    def green(text):
        print(Fore.GREEN + text + Fore.RESET)
    def blue(text):
        print(Fore.YELLOW + text + Fore.RESET)
    def mag(text):
        print(Fore.MAGENTA + text + Fore.RESET)
    def sys(text):
        print(Fore.RED + "System > " + text + Fore.RESET)

def color(text, color):
    if color == 1:
        # Return the text with green color
        return(Fore.GREEN + text + Fore.RESET)

    elif color == 2:
        # Return the text with red color
        return(Fore.RED + text + Fore.RESET)

    elif color == 3:
        # Return the text with magenta color
        return(Fore.MAGENTA + text + Fore.RESET)

    elif color == 4:
        # Return the text with yellow color
        return(Fore.YELLOW + text + Fore.RESET)

    elif color == 5:
        # Return the text with blue color
        return(Fore.BLUE + text + Fore.RESET)


def fwrite(run, filename, content):
    fp = open(filename, 'w')
    fp.write(content)
    fp.close()
    if run == 1: startfile(filename)

def runaspowershell(command, filename):
    fwrite(1, f"{filename}.bat", r'@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "'+command+'"')



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

def cls():
    # Check the current platform
    if platform() == 'Windows':
        # Use the 'cls' command to clear the screen on Windows
        system('cls')
    else:
        # Use the 'clear' command to clear the screen on other platforms
        system('clear')

## download script

def dl(org, url, urlr, name):
    # Download module is located here.
    try:
        download(url, urlr, name)
    except:
        printer.sys("ERROR! : Can't download file from the server...") ; sleep(3)
    try:
        startfile(urlr)
        if org == 1: p1()
        if org == 2: p2()
        if org == 3: p3()
    except:
        printer.sys("ERROR! : Can't start file...") ; sleep(3)
        
## downloader
def download(link, fnam, name):
    def download(link, fnam, name):
        # Check if the file specified by 'fnam' already exists on the file system.
        if isfile(fnam) == False:

            start_time = perf_counter()

            # Parse the URL and convert it to https.
            link = (urlparse(link))._replace(scheme='https').geturl()

            print(Fore.RED + f'[>] Downloading {name}...')

            # Configure an HTTP adapter with retries and connection pooling.
            adapter = HTTPAdapter(max_retries=3,
                                  pool_connections=20,
                                  pool_maxsize=10)

            # Set some headers for the request.
            headers = {'Accept-Encoding': 'gzip, deflate',
                       'User-Agent': 'Mozilla/5.0',
                       'cache_control': 'max-age=600',
                       'connection': 'keep-alive'}

            # Create a new session for the request.
            session = Session()

            # Mount the HTTP adapter to the session.
            session.mount('https://', adapter)

            # Use a context manager to download the file and display the progress.
            with closing(session.get(link,
                                    allow_redirects=True,
                                    stream=True,
                                    headers=headers)) as r:

                # Get the total size of the file.
                total_size = int(r.headers.get('content-length', 0))
                block_size = 4096 # 4 Kibibytes

                # Create a progress bar to display the download progress.

                progress_bar = tqdm(total=total_size, unit='iB', unit_scale=True, bar_format='{desc}: {percentage:3.0f}% │ {bar} │ {n_fmt} / {total_fmt} ║ {elapsed} ─ {remaining} │ {rate_fmt}')

                # Open the file for writing and download the file in chunks.
                with open(fnam, 'wb') as file:
                    for data in r.iter_content(block_size):
                        progress_bar.update(len(data))
                        file.write(data)

                # Close the progress bar and print a message when the download is complete.
                progress_bar.close()
                download_time = perf_counter() - start_time
                print(Fore.RED + f'[>] {name} Downloaded in {round(download_time)}s!')

        # If the file already exists, print a message.
        else:
            print(Fore.RED + f"[>] {name} is already downloaded...")

    with ThreadPoolExecutor() as executor:
        executor.submit(download, link, fnam, name)
        
        


def p1():
  while True:
    cls()
    window11 = color("Windows 11", 1)
    print(f" ┌─────────────────────────────────────────────────────┐\n",
          f"| Made by  X.R. Yong   [W]  Windows                   |\n",
          f"| 1. {window11}    [x64]                              |\n",
          f"| 2. Windows 10    [x64 x32]                          |\n",
          f"| 3. Windows 8.1   [x64]                              |\n",
          f"| 4. Windows 8     [x64]                              |\n",
          f"| 5. Windows 7     [x64]                              |\n",
          f"| 6. Windows 8.1   [x32]                              |\n",
          f"| 7. Windows 8     [x32]                              |\n",
          f"| 8. Windows 7     [x32]                              |\n",
          f"| 9. Windows Vista [x64]                              |\n",
          f"|10. Windows Vista [x32]                              |\n",
          f"|11. Windows XP    [x64]                              |\n",
          f"|12. Windows XP    [x32]                              |\n",
          f"|                                                     |\n",
          f"| [N] - Next Page                                     |\n",
          f"| Example: [W1]                            99 - Exit  |\n",
          f"└─────────────────────────────────────────────────────┘\n")
    choose = input(" > ")
    if achooser(choose, "W1"):  webopen("https://www.microsoft.com/software-download/windows11/")
    elif achooser(choose, "W2"): webopen("https://www.microsoft.com/en-us/software-download/windows10")
    elif achooser(choose, "W3"): dl(1, "https://dl.malwarewatch.org/windows/Windows%208.1%20%28x64%29.iso", "Windows 8.1.iso", "Windows 8.1")
    elif achooser(choose, "W4"): dl(1, "https://dl.malwarewatch.org/windows/Windows%208%20%28x64%29.iso", "Windows 8.iso", "Windows 8")
    elif achooser(choose, "W5"): dl(1, "https://dl.malwarewatch.org/windows/Windows%207%20%28x64%29.iso", "Windows 7.iso", "Windows 7")
    elif achooser(choose, "W6"): dl(1, "https://dl.malwarewatch.org/windows/Windows%208.1.iso", "Windows 8.1.iso", "Windows 8.1")
    elif achooser(choose, "W7"): dl(1, "https://dl.malwarewatch.org/windows/Windows%208.iso", "Windows 8.iso", "Windows 8")
    elif achooser(choose, "W8"): dl(1, "https://dl.malwarewatch.org/windows/Windows%207.iso", "Windows 7.iso", "Windows 7")
    elif achooser(choose, "W9"): dl(1, "https://dl.malwarewatch.org/windows/Windows%20Vista%20%28x64%29.iso", "Windows Vista.iso", "Windows Vista")
    elif achooser(choose, "W10"): dl(1, "https://dl.malwarewatch.org/windows/Windows%20Vista.iso", "Windows Vista.iso", "Windows Vista.iso")
    elif achooser(choose, "W11"): dl(1, "https://dl.malwarewatch.org/windows/Windows%20XP%20%28x64%29.iso", "Windows XP.iso", "Windows XP.iso")
    elif achooser(choose, "W12"): dl(1, "https://dl.malwarewatch.org/windows/Windows%20XP.iso", "Windows XP.iso", "Windows XP")
    elif choose == "N" or choose == "n": p2()

    
    else: runqol(1, choose)

def p2():
  while True:
    cls()
    ech = color("EchoX", 2)
    clr = color("Clear", 1)
    malwarbyte = color("MalwareBytes", 1)
    kaspers = color("Kaspersky", 1)
    ava = color("Avast", 1)
    print(f" ┌────────────────────────────────────────────────────────────────┐\n",
          f"| [A] Antivirus     | [D]  Debloat           | [C] Cleaning      |\n",
          f"| A1. {malwarbyte}  | D1. {ech}              | C1. {clr}         |\n",
          f"| A2. {kaspers}     | D2. O&OWin10Debloat    | C2. CCleaner      |\n",
          f"| A3. {ava}         | D3. WindowsSpyBlocker  |                   |\n",
          f"|                   | D4. Win10Debloat       |                   |\n",
          f"|                                                                |\n",
          f"| [B] - Go Back   [N] - Next Page                                |\n",
          f"| Example: [D1]                              99 - Exit           |\n",
          f"└────────────────────────────────────────────────────────────────┘\n")
    choose = input(" > ")
    if achooser(choose, "D1"):  dl(2, "https://github.com/UnLovedCookie/EchoX/releases/latest/download/EchoX.bat", "EchoX.bat", "EchoX")
    elif achooser(choose, "D2"): dl(2, "https://dl5.oo-software.com/files/ooshutup10/OOSU10.exe", "O&O Shut Up 10.exe", "O&O Shut Up 10")
    elif achooser(choose, "D3"): dl(2,"https://github.com/crazy-max/WindowsSpyBlocker/releases/latest/download/WindowsSpyBlocker.exe", "Windows Spy Blocker.exe", "Windows Spy Blocker")
    elif achooser(choose, "D4"):  runaspowershell("iwr -useb https://git.io/debloat|iex", "Win10Debloat")
    elif achooser(choose, "C1"): dl(2, "https://github.com/XRYong/Clear-Computer/releases/latest/download/clear.bat", "clear.bat", "Clear")
    elif achooser(choose, "A1"): dl(2, "https://www.malwarebytes.com/api/downloads/mb-windows?filename=MBSetup.exe", "MalwareBytesSetup.exe", "MalwareBytes")
    elif achooser(choose, "A2"): webopen("https://usa.kaspersky.com/downloads/free-antivirus")
    elif achooser(choose, "A3"): dl(2, "https://www.avast.com/en-us/download-thank-you.php?product=FAV-ONLINE&locale=en-us&direct=1", "Avast Setup.exe", "Avast")
    elif achooser(choose, "C2"): dl(2, "https://bits.avcdn.net/productfamily_CCLEANER/insttype_FREE/platform_WIN_PIR/installertype_ONLINE/build_RELEASE/cookie_mmm_ccl_008_999_a7a_m", "CCleaner Setup.exe", "CCleaner Setup")
    elif choose == "B" or choose == "b": p1()
    elif choose == "N" or choose == "n": p3()

    
    else: runqol(2, choose)

def p3():
  while True:
    cls()
    rectify_ = color("Rectify 11", 1)
    print(f" ┌─────────────────────────────────────────────────────┐\n",
          f"| Made by  X.R. Yong   [TW]  Tweaked Windows          |\n",
          f"| 1. {rectify_}                                       |\n",
          f"| 2. Windows 11 Debloated                             |\n",
          f"|                                                     |\n",
          f"| [B] - Go Back                                       |\n",
          f"| Example: [TW1]                           99 - Exit  |\n",
          f"└─────────────────────────────────────────────────────┘\n")
    choose = input(" > ")
    if achooser(choose, "TW1"):  dl(3, "https://archive.org/download/rectify-11-v-2/Rectify11%20%28v2%29.iso", "Rectify.iso", "Rectify")
    elif achooser(choose, "TW2"): dl(3, "https://archive.org/download/windows-11-debloated/Windows%2011%20Debloated.iso", "Windows 11 Debloated.iso", "Windows 11 Debloated")
    elif choose == "B" or choose == "b": p2()

    
    else: runqol(3, choose)


def eula():
  cls()

  z = True
  while z == True:
    print("Responsible for your own action...\n",
    "I am not responsible.")

    agree = input("Do you agree? "+Fore.GREEN+"Y "+Fore.RESET+"/ "+Fore.RED+"n"+Fore.RESET+": ")

    if achooser(agree, "y"):
            print("You agreed to the EULA.")
            z = False
        
        # If the user does not agree, exit the program
    elif achooser(agree, "n"):
      print("Ok, come back if you change your mind."); exit(sleep(3))
    elif achooser(agree, "Y_CMD") or achooser(agree, "Y&CMD") or achooser(agree, "&"): z = False ; cls() ; cmd.console()
    elif achooser(agree, "~"): z = False ; cls() ; cmd.console()
    elif achooser(agree, "sp"): z = False ; cls() ; cmd.uicmdcs()
        # If the user's input is not "y" or "n", call the runqol() function
    else: runqol(0, agree)
    
    # Delete the variable z
  del z


def prep():
  if ping("github.com") == None or False:
    if ping("google.com") == None or False:
      print("No Internet!")
      sleep(3)
      exit()


version = "6"
dev_v = ""
dev_alpha = ""
devmd = False
Fastst = False

if devmd == True:
    printer.sys("Devoloper Mode. Not Checking For Updates...")
else:
    prep()
    newer = latest("XRYong/Windows-Utility")
    printer.sys("Checking For Update...")
    if version == str(newer):
        printer.sys("Up-to-date!")
    elif str(newer) > version:
        printer.sys("Outdated...")
        printer.sys("Loading Updater...")
        dl(0, "https://github.com/XRYong/Windows-Utility/releases/latest/download/windows-utility.exe", "Windows Utility"+str(newer)+".exe", "Windows Utility Update")
        exit()

def start():
  window11 = color("Windows 11", 1)
  ech = color("EchoX", 2)
  clr = color("Clear", 1)
  malwarbyte = color("MalwareBytes", 1)
  kaspers = color("Kaspersky", 1)
  rectify_ = color("Rectify 11", 1)
  ava = color("Avast", 1)
  printer.sys("Starting...")
  printer.sys("Loading Eula...")
  printer.sys("Running Network Check...")
  prep()
  com.ping()
  printer.sys("Almost Done...")
  printer.sys("Done Loading!")
  printer.sys("Loading Eula...")
  printer.sys("Done Loading!")
  eula()
  p1()

class dev:
    def dev_md_cs_1():
        p1()
    def dev_md_cs_2():
        p2()
    def dev_md_cs_3():
        p3()

def ns():
    p1()

if devmd == False and Fastst == False:    
  window11 = color("Windows 11", 1)
  ech = color("EchoX", 2)
  clr = color("Clear", 1)
  malwarbyte = color("MalwareBytes", 1)
  kaspers = color("Kaspersky", 1)
  rectify_ = color("Rectify 11", 1)
  ava = color("Avast", 1)
  start()
elif devmd == True:
  print(Fore.RED + "Danger! Devoloper Mode is enabled." + Fore.RESET)
  cmd.uicmdcs()
elif Fastst == True:
    print(Fore.RED + "Danger! Fast Mode is enabled." + Fore.RESET)
    bootodr.fast_odr()