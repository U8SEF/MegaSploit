#--------------------------------------------------------------#
# ============================================================ #
# =================# < MEGASPLOIT  1.0.0 > #================== #
# ============================================================ #
# ================== < By: Youssef Ahmed > =================== #
# ============================================================ #
#--------------------------------------------------------------#

import os
import sys
import time
import modules.Packager as Packager

#=-----=#

__Version__ = "1.0.0"
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[39m"

#=-----=#
os.system("")
PLATFORM = sys.platform
if PLATFORM == "win32":
    print(f"{RED}[{YELLOW}+{RED}]{RESET}" +" Sorry Metasploit Is Not Supported For Windows" +RESET)
    sys.exit()
MISSING = False
LIBS = []
try:
    import pystyle
    PYSTYLE = GREEN + "OK" + RESET
except:
    PYSTYLE = RED + "Missing" +RESET
    LIBS.append("pystyle")
    MISSING = True
try:
    import requests
    REQUESTS = GREEN + "OK" + RESET
except:
    REQUESTS = RED + "Missing" +RESET
    LIBS.append("requests")
    MISSING = True
try:
    import InquirerPy
    INQUIRERPY = GREEN + "OK" + RESET
except:
    INQUIRERPY = RED + "Missing" +RESET
    LIBS.append("InquirerPy")
    MISSING = True
if os.path.exists("/etc/alternatives/msfconsole"):
    METASPLOIT =  GREEN + "OK" +RESET

else:
    METASPLOIT = RED + "Missing" +RESET
    MISSING = True

#=-----=#
print(f"{RED}[{YELLOW}+{RED}] {RESET}Starting...!")
time.sleep(1)
print(f"{RED}[{YELLOW}+{RED}]{RESET}" + " PyStyle".ljust(20, ".") +PYSTYLE)
time.sleep(0.4)
print(f"{RED}[{YELLOW}+{RED}]{RESET}" +" Requests".ljust(20, ".") +REQUESTS)
time.sleep(0.4)
print(f"{RED}[{YELLOW}+{RED}]{RESET}" +" InquirerPy".ljust(20, ".") +INQUIRERPY)
time.sleep(0.4)
print(f"{RED}[{YELLOW}+{RED}]{RESET}" +" Metasploit".ljust(20, ".") +METASPLOIT)
if MISSING:
    time.sleep(1)
    print(f"{RED}[{YELLOW}!{RED}] Dependency Installation Failed..!{RESET}")
    time.sleep(1)
    print(f"{RED}[{YELLOW}!{RED}] Problems Are Attempted To Be Solved..!{RESET}")
    time.sleep(1)
    for i in LIBS:
        Packager.install(i)
    import modules.CLI as CLI
    CLI.run(_version_=__Version__)
