#!usr/bin/env python

import subprocess
import optparse
import colorama
from colorama import Fore, Back, Style
colorama.init()

# Set the color semi-permanently

print(Style.RESET_ALL)
print(Fore.RED + '''
 __  __    __    ___    ___  ____  _____  _____  ____  ____  ____    ____  _  _ 
(  \/  )  /__\  / __)  / __)(  _ \(  _  )(  _  )( ___)( ___)(  _ \  (  _ \( \/ )
 )    (  /(__)\( (__   \__ \ )___/ )(_)(  )(_)(  )__)  )__)  )   /   ) _ < \  / 
(_/\/\_)(__)(__)\___)  (___/(__)  (_____)(_____)(__)  (____)(_)\_)  (____/ (__) 
''' + Style.RESET_ALL)



print(Fore.CYAN + Back.BLACK)
print('''
  /$$$$$$      /$$   /$$           /$$$$$$$$        /$$       /$$                           /$$
 /$$__  $$    |__/  | $$          |__  $$__/       | $$      |__/                          | $$
| $$  \ $$ /$$ /$$ /$$$$$$           | $$  /$$$$$$ | $$$$$$$  /$$ /$$   /$$  /$$$$$$   /$$$$$$$
| $$$$$$$$|__/| $$|_  $$_/           | $$ |____  $$| $$__  $$| $$| $$  | $$ |____  $$ /$$__  $$
| $$__  $$ /$$| $$  | $$             | $$  /$$$$$$$| $$  \ $$| $$| $$  | $$  /$$$$$$$| $$  | $$
| $$  | $$| $$| $$  | $$ /$$         | $$ /$$__  $$| $$  | $$| $$| $$  | $$ /$$__  $$| $$  | $$
| $$  | $$| $$| $$  |  $$$$/         | $$|  $$$$$$$| $$$$$$$/| $$|  $$$$$$$|  $$$$$$$|  $$$$$$$
|__/  |__/| $$|__/   \___/           |__/ \_______/|_______/ |__/ \____  $$ \_______/ \_______/
     /$$  | $$                                                    /$$  | $$                    
    |  $$$$$$/                                                   |  $$$$$$/                    
     \______/                                                     \______/                     
''')

print(Style.RESET_ALL)

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface To change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, Use --help fore more info.")
    elif not options.new_mac:
        parser.error("[-]Please specify a new mac, Use --help fore more info.")
    return options


def change_mac(interface, new_mac):
    print("[+] Changing MAC Address For " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


options = get_arguments()
change_mac(options.interface, options.new_mac)
