import os


def aircrackwifi():

    logo = r'''
    _    _                         _       ___       _                          _             
   / \  (_)_ __ ___ _ __ __ _  ___| | __  |_ _|_ __ | |_ ___ _ __ ___ ___ _ __ | |_ ___  _ __ 
  / _ \ | | '__/ __| '__/ _` |/ __| |/ /   | || '_ \| __/ _ \ '__/ __/ _ \ '_ \| __/ _ \| '__|
 / ___ \| | | | (__| | | (_| | (__|   <    | || | | | ||  __/ | | (_|  __/ |_) | || (_) | |   
/_/   \_\_|_|  \___|_|  \__,_|\___|_|\_\  |___|_| |_|\__\___|_|  \___\___| .__/ \__\___/|_|   
                                                                          |_|                  
    Special for Cyber Sec`s by F4RB3R
    '''

    os.system("clear")
    print(logo)

    print("Kill network manager ? (type 'y' or 'n')")

    if input() == "y":
        os.system("airmon-ng check kill")
    elif input() == "yes":
        os.system("airmon-ng check kill")
    else:
        print("Network manager wasn`t stopped !")

    os.system("airmon-ng")

    print("Select wifi-dongle that is more powerful ! (0 for wlan0, 1 for wlan1 and 2 for wlan2)")

    userdecision = input()

    if userdecision == "0":
        os.system("airmon-ng start wlan0")
    elif userdecision == "1":
        os.system("airmon-ng start wlan1")
    elif userdecision == "2":
        os.system("airmon-ng start wlan2")
    else:
        print("You didn`t choose wifi-dongle !\nExiting...")
        exit()

    os.system("airodump-ng wlan" + userdecision + "mon")
