from tools.userdork import userdork
from tools.ftpscanner import ftpscanner
from tools.androiddb import androiddb
from tools.printerhp import printerhp
import os
import platform


logo = (r"""
       _____ _    _  ____  _____          _   _     _____  _____          _   _ _   _ ______ _____  
      / ____| |  | |/ __ \|  __ \   /\   | \ | |   / ____|/ ____|   /\   | \ | | \ | |  ____|  __ \ 
     | (___ | |__| | |  | | |  | | /  \  |  \| |  | (___ | |       /  \  |  \| |  \| | |__  | |__) |
      \___ \|  __  | |  | | |  | |/ /\ \ | . ` |   \___ \| |      / /\ \ | . ` | . ` |  __| |  _  / 
      ____) | |  | | |__| | |__| / ____ \| |\  |   ____) | |____ / ____ \| |\  | |\  | |____| | \ \ 
     |_____/|_|  |_|\____/|_____/_/    \_\_| \_|  |_____/ \_____/_/    \_\_| \_|_| \_|______|_|  \_\
                                                                                                    
                                                                                                     
      * Find and Exploit                                                           Created by F4RB3R
    """)

# Create logs folder
if not os.path.exists('logs'):
    os.mkdir('logs')


# Main
def shodanscanner():
    try:
        if platform.system() == "Windows":
            os.system("@cls")
        else:
            os.system("clear")
        print(logo)

        print('''
        [1] Vulnerable FTP
         
        [2] Android Debug Bridge
         
        [3] HP Printers
         
        [4] Own search dork
         
        [99] Exit
        ''')

        menu_option = int(input('[OPTION] ==> '))
        if menu_option == 1:
            ftpscanner()
        elif menu_option == 2:
            androiddb()
        elif menu_option == 3:
            printerhp()
        elif menu_option == 4:
            userdork()
        else:
            exit()
            print('[$] Created by F4RB3R with Love.')

    except KeyboardInterrupt:
        print('\n[!] (Ctrl + C) detected.. Stopping...')
        print('[$] Created by F4RB3R with Love.')
