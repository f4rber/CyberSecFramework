import os
from modules.CyberScanner import portscanner
from modules.AircrackWifi import aircrackwifi
from modules.AirodumpWifi import airodumpwifi
from modules.nmapscanner import nmap
from ShodanScanner import shodanscanner
from CensysScanner import censysscanner


if os.geteuid() != 0:
    exit("You need to have root privileges to run this script.\nPlease try again, this time using 'sudo'. Exiting.")


mainlogo = r'''
  ____      _                  ____                _____                                            _    
 / ___|   _| |__   ___ _ __   / ___|  ___  ____   |  ___| __ __ _ _ __ ___   _____      _____  _ __| | __
| |  | | | | '_ \ / _ \ '__|  \___ \ / _ \/ __|   | |_ | '__/ _` | '_ ` _ \ / _ \ \ /\ / / _ \| '__| |/ /
| |__| |_| | |_) |  __/ |      ___) |  __/ (__    |  _|| | | (_| | | | | | |  __/\ V  V / (_) | |  |   < 
 \____\__, |_.__/ \___|_|     |____/ \___|\___|   |_|  |_|  \__,_|_| |_| |_|\___| \_/\_/ \___/|_|  |_|\_\
      |___/    
'''


def automatedmetasploit():
    os.system("./modules/automatedmetsaploit")


# Main
def main():
    os.system("clear")
    print(mainlogo)

    print('''
 [1] Port Scanner
 
 [2] nmap Scanner

 [3] Capture Handshake Of The Closest Networks  

 [4] Capture Handshake Of Specific Network

 [5] Automated Metasploit
 
 [6] Shodan Scanner
 
 [7] Censys Scanner

 [99] Exit
''')

    menu_option = int(input('[OPTION] ==> '))
    if menu_option == 1:
        portscanner()
    elif menu_option == 2:
        nmap()
    elif menu_option == 3:
        aircrackwifi()
    elif menu_option == 4:
        airodumpwifi()
    elif menu_option == 5:
        automatedmetasploit()
    elif menu_option == 6:
        shodanscanner()
    elif menu_option == 7:
        censysscanner()
    elif menu_option == 99:
        exit()
    else:
        print("Wrong command !")


if __name__ == '__main__':
    main()
    print('[$] Created by F4RB3R with Love.')
