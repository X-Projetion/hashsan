import os
import hashlib
from datetime import datetime

""" ANSI color codes """
BLACK = "\033[0;30m"
RED = "\033[0;31m"
GREEN = "\033[0;32m"
BROWN = "\033[0;33m"
BLUE = "\033[0;34m"
PURPLE = "\033[0;35m"
CYAN = "\033[0;36m"
LIGHT_GRAY = "\033[0;37m"
DARK_GRAY = "\033[1;30m"
LIGHT_RED = "\033[1;31m"
LIGHT_GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
LIGHT_BLUE = "\033[1;34m"
LIGHT_PURPLE = "\033[1;35m"
LIGHT_CYAN = "\033[1;36m"
LIGHT_WHITE = "\033[1;37m"
BOLD = "\033[1m"
FAINT = "\033[2m"
ITALIC = "\033[3m"
UNDERLINE = "\033[4m"
BLINK = "\033[5m"
NEGATIVE = "\033[7m"
CROSSED = "\033[9m"
END = "\033[0m"

def print_banner():
    os.system('cls' if os.name == 'nt' else 'clear')
    banner = """
    {RED}__  __           __   {GREEN}_____           
   {RED}/ / / /___ ______/ /_ {GREEN}/ ___/ ____ _____ 
  {RED}/ /_/ / __ `/ ___/ __ \\{GREEN}\\__ \\\/ __ `/ __ \\
 {RED}/ __  / /_/ (__  ) / / /{GREEN}___/ / /_/ / / / /
{RED}/_/ /_/\\__,_/____/_/ /_/{GREEN}/____/\\__,_/_/ /_/ v1
            {YELLOW}github.com/X-Projetion
    """.format(RED=RED, GREEN=GREEN, YELLOW=YELLOW)
    print(banner)

def print_with_timestamp(message):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"{RED}[{YELLOW}{timestamp}{RED}]{END} {message}")

def crack_password(target_hashes, wordlist_path, output_file=None):
    found_passwords = {}
    with open(wordlist_path, "r", encoding="latin-1") as wordlist_file:
        for line in wordlist_file:
            password = line.strip()
            hashed_password = hashlib.md5(password.encode()).hexdigest()
            if hashed_password in target_hashes:
                found_passwords[hashed_password] = password

    if found_passwords:
        print_with_timestamp(LIGHT_CYAN + "[INFO]" + GREEN + " Password(s) ditemukan:")
        for hashed_password, password in found_passwords.items():
            print_with_timestamp(LIGHT_CYAN + "[INFO]" + GREEN + f" Hash: {hashed_password}:{password}")
        if output_file:
            with open(output_file, "w") as output:
                for hashed_password, password in found_passwords.items():
                    output.write(f"{hashed_password}:{password}\n")
    else:
        print_with_timestamp(LIGHT_CYAN + "[INFO]" + RED + " Password tidak ditemukan dalam wordlist.")
