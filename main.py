import argparse
from library.exp import crack_password, print_banner, print_with_timestamp
from colorama import init
init(autoreset=True)

def main():
    parser = argparse.ArgumentParser(description="Simple password cracker using a wordlist", add_help=False)
    parser.add_argument("-h", "--help", action="help", help="Show this help message and exit")
    parser.add_argument("-o", "--output", help="Output file for cracked passwords")
    parser.add_argument("-w", "--wordlist", help="Path to the wordlist file", default="wordlist.txt")
    parser.add_argument("-p", "--hash", help="Target hash to crack")
    parser.add_argument("-l", "--hashlist", help="Path to the hash list file")
    args = parser.parse_args()

    print_banner()

    output_file = args.output
    wordlist_path = args.wordlist
    target_hash = args.hash
    hashlist_path = args.hashlist

    target_hashes = set()

    if target_hash:
        if hashlist_path:
            print_with_timestamp("\033[0;31mAnda tidak dapat menggunakan argumen -p dan -l bersama.\033[0m")
        else:
            target_hashes.add(target_hash)
    elif hashlist_path:
        with open(hashlist_path, "r") as hashlist_file:
            for line in hashlist_file:
                hashed_password = line.strip()
                target_hashes.add(hashed_password)

    if target_hashes:
        try:
            crack_password(target_hashes, wordlist_path, output_file)
        except FileNotFoundError:
            print_with_timestamp("\033[0;31mFile wordlist tidak ditemukan.\033[0m")
    else:
        print_with_timestamp("\033[0;33mSilakan berikan hash target dengan opsi -p atau file hash list dengan opsi -l untuk melanjutkan atau opsi -h untuk bantuan.\033[0m")

if __name__ == "__main__":
    main()
