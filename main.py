#!/usr/bin/python
import itertools
import argparse
from colorama import Fore
import string

# Argparse
parser = argparse.ArgumentParser(prog = 'Passsword List Generator For BruteForce')
parser.add_argument('-min', '--min', help='Min Length of Password (default = 3)', dest='min', type=int, default='3')
parser.add_argument('-max', '--max', help='Max Length of Password', dest='max', type=int, required=True)
parser.add_argument('-t', '--type', help='Letters = 1, Numbers = 2, Symbols = 3 (ex. 1/3)', dest='type', default='1/2/3', required=True)
parser.add_argument('-f', '--file', help='Name Of File To Save Password', dest='file', default='passwords.txt')

# Variables
file_name = parser.parse_args().file
let_type = parser.parse_args().type
min_length = parser.parse_args().min
max_length = parser.parse_args().max
symbols = [string.ascii_letters, string.digits, string.punctuation]

# Generate Passwords
def make_passlist(max_length, min_length):
    try:
        types = let_type.split('/')
        password_list = "".join([symbols[int(i) - 1] for i in types])

        with open(file_name, 'w+') as file:
            print(f'{Fore.LIGHTGREEN_EX}Starting Password Generation:\n')
            for length in range(int(min_length), int(max_length) + 1):
                for password in itertools.product(password_list, repeat=length):
                    file.write(''.join(password)+ '\n')

        print(f"{Fore.LIGHTMAGENTA_EX}Passwords Was Saved In {file_name}")

    except Exception as ex:
        print(f' {Fore.LIGHTRED_EX}Error Happened exiting...')

def main():
    make_passlist(min_length=min_length, max_length=max_length)

if __name__ == '__main__':
    main()
