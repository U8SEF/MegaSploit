import os
import shutil
import requests

#=-----=#

try:
    os.remove("MegaSploit.py")
except:
    pass
try:
    shutil.rmtree("modules")
except:
    pass
try:
    os.mkdir("modules")
except:
    pass

#################################
##      MegaSploit File        ##
#################################

MegaSploit_File = requests.get("https://raw.githubusercontent.com/U8SEF/MegaSploit/main/MegaSploit.py").content
Mega = open("MegaSploit.py", 'wb')
Mega.write(MegaSploit_File)
Mega.close()

#################################
##           Cli File          ##
#################################

Cli_File = requests.get("https://raw.githubusercontent.com/U8SEF/MegaSploit/main/modules/CLI.py").content
Cli = open("modules/CLI.py", 'wb')
Cli.write(Cli_File)
Cli.close()

#################################
##        Packager File        ##
#################################

Packager_File = requests.get("https://raw.githubusercontent.com/U8SEF/MegaSploit/main/modules/Packager.py").content
Packager = open("modules\\Packager.py", 'wb')
Packager.write(Packager_File)
Packager.close()