"""
Parke
07/15/2024
SHA-256 Hash Cracking Tool
Inspired by CodeWars 'SHA-256 Cracker' Kata, customized for a more tailored experience
"""


import hashlib
import argparse
from colorama import init, Fore


# Initiate colorama colors
init()
GREEN = Fore.GREEN
RED = Fore.RED

print("\n")
print("@@@@@@   @@@  @@@   @@@@@@    @@@@@@   @@@@@@@    @@@@@@              @@@@@@@  @@@@@@@    @@@@@@    @@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@")
print("@@@@@@@   @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@   @@@@@@@             @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@@@@@@  @@@@@@@@")
print("!@@       @@!  @@@  @@!  @@@       @@@  !@@      !@@                  !@@       @@!  @@@  @@!  @@@  !@@       @@!  !@@  @@!       @@!  @@@")
print("!@!       !@!  @!@  !@!  @!@      @!@   !@!      !@!                  !@!       !@!  @!@  !@!  @!@  !@!       !@!  @!!  !@!       !@!  @!@")
print("!!@@!!    @!@!@!@!  @!@!@!@!     !!@    !!@@!!   !!@@!@!   @!@!@!@!@  !@!       @!@!!@!   @!@!@!@!  !@!       @!@@!@!   @!!!:!    @!@!!@!")
print(" !!@!!!   !!!@!!!!  !!!@!!!!    !!:     @!!@!!!  @!!@!!!!  !!!@!@!!!  !!!       !!@!@!    !!!@!!!!  !!!       !!@!!!    !!!!!:    !!@!@!")
print("     !:!  !!:  !!!  !!:  !!!   !:!          !:!  !:!  !:!             :!!       !!: :!!   !!:  !!!  :!!       !!: :!!   !!:       !!: :!!")
print("    !:!   :!:  !:!  :!:  !:!  :!:           !:!  :!:  !:!             :!:       :!:  !:!  :!:  !:!  :!:       :!:  !:!  :!:       :!:  !:!")
print(":::: ::   ::   :::  ::   :::  :: :::::  :::: ::  :::: :::              ::: :::  ::   :::  ::   :::   ::: :::   ::  :::   :: ::::  ::   :::")
print(":: : :     :   : :   :   : :  :: : :::  :: : :    :: : :               :: :: :   :   : :   :   : :   :: :: :   :   :::  : :: ::    :   : :")
print("\n\n")


##############################################################
# Function: Uses hashlib module to loop through wordlist     #
#           passed as first CLI arg and hash each value to   #
#           compare to original hash passed as second CLI    #
#           arg until a match is found or all words have     #
#           been used. Can pass a file of hash lists as well #
#                                                            #
# Param(s): Hash from original string or hash list and       #
#           wordlist to use in cracking attempts             #
#                                       `                    #
# Return: Original cracked string or list of cracked strings #
#         if found, None otherwise                           #
##############################################################
def sha256_cracker(wordlist, our_hash, hash_list):

    clear_text_file = None

    if hash_list:
        hashes = open(hash_list, "r").read().splitlines()

        for hash_element in hashes:
            for plaintext in wordlist:
                hashed_element = hashlib.sha256(plaintext.encode()).hexdigest()

                if hashed_element.lower() == hash_element.lower():
                    print(f"{GREEN}[+] Hash Cracked: Hash is " + hash_element + " - Plaintext is " + plaintext)
                    clear_text_file = open("cracked_hashes.txt", "a")
                    clear_text_file.write(f"{GREEN}Hash: " + hash_element + " - Plaintext: " + plaintext + "\n")
                    break

        if not clear_text_file:
            print(f"{RED}[!] No hashes were found with the given wordlist. Try another one")
            return None

        if clear_text_file:
            print(f"{GREEN}\nCracked hashes saved to 'cracked_hashes.txt' in current working directory")
        return

    if our_hash:
        for element in wordlist:
            hashed_element = hashlib.sha256(element.encode()).hexdigest()
            if hashed_element.lower() == our_hash.lower():
                print(f"{GREEN}[+] Hash Cracked: Hash is " + element)
                return element
        print(f"{RED}[!] Hash Not Found")
        return None


# Initiate parser object and add custom arguments
parser = argparse.ArgumentParser()
parser.add_argument("-w", "--wordlist", type=str, required=True,
                    help="File of plaintext passwords to try cracking with")

parser.add_argument("-hash", "--single_hash", type=str,
                    help="Single SHA-256 hash you want to crack")

parser.add_argument("-f", "--file_of_hashes", type=str,
                    help="File of SHA-256 hashes you want to crack")

args = parser.parse_args()
pass_file = args.wordlist
hash_to_crack = args.single_hash
hash_file = args.file_of_hashes


# Used for single hash cracking attempt
if hash_to_crack:
    file = open(pass_file, "r").read().splitlines()
    cracked_hash = sha256_cracker(file, hash_to_crack, None)
    if cracked_hash:
        open("cracked_hash.txt", "w").write(f"{GREEN}Hash: " + hash_to_crack + " - Plaintext: " + cracked_hash + "\n")
        print(f"\n{GREEN}Cracked hash saved to 'cracked_hash.txt' in current working directory")

# Used for file of multiple hashes to attempt cracking
if hash_file:
    file = open(pass_file, "r").read().splitlines()
    sha256_cracker(file, None, hash_file)
