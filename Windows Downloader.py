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
from time import perf_counter
from urllib.parse import urlparse


start = default_timer


try:
    from colorama import Fore, init
    from tqdm import tqdm
    from requests import Session
    from requests.adapters import HTTPAdapter
except:
    system("pip install -U colorama tqdm requests")



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
    try:
        download(url, urlr, name)
        startfile(urlr)
    except:
        print("Bad Error! Please restart program!") ; sleep(3)
        exit()
        

def download(link, fnam, name):
    def download(link, fnam, name):
        # Check if the file specified by 'fnam' already exists on the file system.
        if isfile(fnam) == False:

            start_time = perf_counter()

            # Parse the URL and convert it to https.
            link = (urlparse(link))._replace(scheme='https').geturl()

            print(Fore.GREEN + f'[>] Downloading {name}...' + Fore.RESET)

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
                print(Fore.GREEN + f'[>] {name} Downloaded in {round(download_time)}s!' + Fore.RESET)

        # If the file already exists, print a message.
        else:
            print(Fore.RED + f"[>] {name} is already downloaded..." + Fore.RESET)

    with ThreadPoolExecutor() as executor:
        executor.submit(download, link, fnam, name)


def p1():
  while True:
    cles()
    print(Fore.RESET + " ┌─────────────────────────────────────────────────────┐\n",
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
          "| [N] - Next Page                                     |\n",
          "| Example: [W1]                            99 - Exit  |\n",
          "└─────────────────────────────────────────────────────┘\n")
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
    cles()
    print(" ┌─────────────────────────────────────────────────────┐\n",
          "| Made by  X.R. Yong   [D]  Debloat                   |\n",
          "| 1. Echo X                                           |\n",
          "| 2. O&O Shut 10                                      |\n",
          "| 3. Windows Spy Blocker                              |\n",
          "|                                                     |\n",
          "| [B] - Go Back   [N] - Next Page                     |\n",
          "| Example: [D1]                            99 - Exit  |\n",
          "└─────────────────────────────────────────────────────┘\n")
    choose = input(" > ")
    if achooser(choose, "D1"):  dl(2, "https://github.com/UnLovedCookie/EchoX/releases/latest/download/EchoX.bat", "EchoX.bat", "EchoX")
    elif achooser(choose, "D2"): dl(2, "https://dl5.oo-software.com/files/ooshutup10/OOSU10.exe", "O&O Shut Up 10.exe", "O&O Shut Up 10")
    elif achooser(choose, "D3"): dl(2,"https://github.com/crazy-max/WindowsSpyBlocker/releases/latest/download/WindowsSpyBlocker.exe", "Windows Spy Blocker.exe", "Windows Spy Blocker")
    elif choose == "B" or choose == "b": p1()
    elif choose == "N" or choose == "n": p3()

    
    else: runqol(2, choose)

def p3():
  while True:
    cles()
    print(" ┌─────────────────────────────────────────────────────┐\n",
          "| Made by  X.R. Yong   [TW]  Tweaked Windows          |\n",
          "| 1. Rectify 11                                       |\n",
          "| 2. Windows 11 Debloated                             |\n",
          "|                                                     |\n",
          "| [B] - Go Back                                       |\n",
          "| Example: [TW1]                           99 - Exit  |\n",
          "└─────────────────────────────────────────────────────┘\n")
    choose = input(" > ")
    if achooser(choose, "TW1"):  dl(3, "https://archive.org/download/rectify-11-v-2/Rectify11%20%28v2%29.iso", "Rectify.iso", "Rectify")
    elif achooser(choose, "TW2"): dl(3, "https://archive.org/download/windows-11-debloated/Windows%2011%20Debloated.iso", "Windows 11 Debloated.iso", "Windows 11 Debloated")
    elif choose == "B" or choose == "b": p2()

    
    else: runqol(3, choose)


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

