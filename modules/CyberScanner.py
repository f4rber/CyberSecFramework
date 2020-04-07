import socket
import platform
import os
import sys
from datetime import datetime


def portscanner():

    logo = r'''
  ____      _                  ____                                  
 / ___|   _| |__   ___ _ __   / ___|  ___ __ _ _ __  _ __   ___ _ __ 
| |  | | | | '_ \ / _ \ '__|  \___ \ / __/ _` | '_ \| '_ \ / _ \ '__|
| |__| |_| | |_) |  __/ |      ___) | (_| (_| | | | | | | |  __/ |   
 \____\__, |_.__/ \___|_|     |____/ \___\__,_|_| |_|_| |_|\___|_|   
       |___/                                                                                                      
    Special for Cyber Sec`s by F4RB3R
    '''

    if platform.system() == "Windows":
        os.system("@cls")
    else:
        os.system("clear")
    print(logo)

    remoteServer = input("Enter a remote host to scan: ")
    remoteServerIP = socket.gethostbyname(remoteServer)

    print("-" * 60)
    print("Please wait, scanning remote host", remoteServerIP)
    print("-" * 60)

    t1 = datetime.now()

    dict = [20, 21, 22, 53, 80, 443, 445, 3389, 25]

    try:
        for port in dict:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((remoteServerIP, port))
            if result == 0:
                print("Port {}: 	Open".format(port))
            sock.close()

    except KeyboardInterrupt:
        print("You pressed Ctrl+C")
        sys.exit()

    except socket.gaierror:
        print('Hostname could not be resolved. Exiting')
        sys.exit()

    except socket.error:
        print("Couldn't connect to server")
        sys.exit()

    t2 = datetime.now()

    total = t2 - t1

    print('Scanning Completed in: ', total)
