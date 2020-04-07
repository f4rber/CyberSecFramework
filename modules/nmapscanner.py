import os


def a():
    hostsv = input("Enter host:\n")
    savesv = input("Save output to txt file? (y or n)\n")
    if savesv == "y":
        filepath = input("Enter the location for the file and filename\nExample: /home/kali/Desktop/output.txt")
        os.system("nmap -oN " + filepath + " -A " + str(hostsv))
    else:
        os.system("nmap -A " + str(hostsv))


def ss():
    hostsv = input("Enter host:\n")
    savesv = input("Save output to txt file? (y or n)\n")
    if savesv == "y":
        filepath = input("Enter the location for the file and filename\nExample: /home/kali/Desktop/output.txt")
        os.system("nmap -oN " + filepath + " -sS " + str(hostsv))
    else:
        os.system("nmap -sS " + str(hostsv))


def sv():
    hostsv = input("Enter host:\n")
    savesv = input("Save output to txt file? (y or n)\n")
    if savesv == "y":
        filepath = input("Enter the location for the file and filename\nExample: /home/kali/Desktop/output.txt")
        os.system("nmap -oN " + filepath + " -sV " + str(hostsv))
    else:
        os.system("nmap -sV " + str(hostsv))


def asssv():
    hostsv = input("Enter host:\n")
    savesv = input("Save output to txt file? (y or n)\n")
    if savesv == "y":
        filepath = input("Enter the location for the file and filename\nExample: /home/kali/Desktop/output.txt")
        os.system("nmap -oN " + filepath + " -A -sS -sV " + str(hostsv))
    else:
        os.system("nmap -A -sS -sV " + str(hostsv))


def ownsample():
    hostsv = input("Enter host:\n")
    usersample = input("Enter option for nmap\nExample: -sS\n")
    savesv = input("Save output to txt file? (y or n)\n")
    if savesv == "y":
        filepath = input("Enter the location for the file and filename\nExample: /home/kali/Desktop/output.txt")
        os.system("nmap -oN " + filepath + " " + usersample + " " + str(hostsv))
    else:
        os.system("nmap " + usersample + " " + str(hostsv))


def ownsampletxt():
    pathtofile = input("Enter path to txt file\nExample: /home/kali/Desktop.txt")
    usersample = input("Enter option for nmap\nExample: -sS\n")
    savesv = input("Save output to txt file? (y or n)\n")
    if savesv == "y":
        filepath = input("Enter the location for the file and filename\nExample: /home/kali/Desktop/output.txt")
        os.system("nmap -oN " + filepath + " " + usersample + " " + str(pathtofile))
    else:
        os.system("nmap " + usersample + " " + str(pathtofile))


def nmap():
    print(r'''             
             _                                     
            | |                                    
  __ _ _   _| |_ ___  _ __  _ __ ___   __ _ _ __   
 / _` | | | | __/ _ \| '_ \| '_ ` _ \ / _` | '_ \  
| (_| | |_| | || (_) | | | | | | | | | (_| | |_) | 
 \__,_|\__,_|\__\___/|_| |_|_| |_| |_|\__,_| .__/  
                                           | |     
                                           |_|     
''')
    print('''
     [1] nmap -A host

     [2] nmap -sS host

     [3] nmap -sV host

     [4] nmap -A -sS -sV host

     [5] Own sample
     
     [6] Scan ip`s from txt

     [99] Exit
    ''')

    menu_option = int(input('[OPTION] ==> '))
    if menu_option == 1:
        a()
    elif menu_option == 2:
        ss()
    elif menu_option == 3:
        sv()
    elif menu_option == 4:
        asssv()
    elif menu_option == 5:
        ownsample()
    elif menu_option == 6:
        ownsampletxt()
    elif menu_option == 99:
        exit()
    else:
        print("Wrong command !")
