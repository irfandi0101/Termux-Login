import os
import time

from getpass import getpass

def menu():
    os.system('clear')
    print('\033[1;36;40m  v.1.1  [█ █ █ █ █ █ █ █ █ █ █ █ █ █]')   
    print("")
    
    print('\033[1;92m    786 => bismi-llāhir-raḥmānir-raḥīm')
    print("\033[1;93m")
    print("  << --------Assalamu-Alaikum---------->>")
    print("\033[1;96m")
    x = input('\033[1;92mUsername \033[1;93m: ')
    print("")
    o = input("Are you want to show your password [ y/n ] : ")
    print("")
    if o=="y":
        e = input('\033[1;92mPassword \033[1;93m: ')
    elif o=="n":
        e = getpass('\033[1;92mPassword \033[1;93m: ')

    if x=="muju" and e=="123":
        print('')
        print('    welcome ========>',x)
        print("")
    else:
         print("")
         print("\033[1;91m       You can't Access my Termux privacy 😜")
         time.sleep(2)
         os.system('ps')
         os.system('killall -9 com.termux')
menu()
