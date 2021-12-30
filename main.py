import itertools
import sys
from string import digits, punctuation, ascii_letters
import time
# from bs4 import BeautifulSoup
# import requests
from datetime import datetime

l = 0

syimvols = [digits, punctuation, ascii_letters]
# print(len(sys.argv))
if len(sys.argv) < 2:
    file_name = "pass.txt"

elif len(sys.argv) >= 2:
    file_name = sys.argv[1]


def bruetforce_exel():
    # rl = BeautifulSoup(src, "lxml")
    print("*****bad_Brut*****")
    qu = input("start?(y n): ")
    if qu == "n":
        exit()
    try:
        
        brut_length = input("input nmu_1 && num-2: ")
        brut_length = [int(item) for item in brut_length.split('-')]


    except:
        print("try again")
        bruetforce_exel()


    r = int(input("if only number enter 0\nif only text type 1"
        "\nif only !@# type 2\nif all of this type 3\n4 your variant\n"))
    if r > 4:
        exit()
    if r == 4:
        r_5 = str(input("type here: "))

    if r == 0:
        l = syimvols[0]
    elif r == 1:
        l = syimvols[2]
    elif r == 2:
        l = syimvols[1]
    elif r == 3:
        l = syimvols[0] + syimvols[1] + syimvols[2]
    elif r == 4:
        j = [int(item) for item in r_5.split("+")]
        l = syimvols[j[0]] + syimvols[j[1]]



    star_time = time.time()
    count = 0
    print(f"Started at {datetime.utcfromtimestamp(time.time()).strftime('%H:%M:%S')}")
#   brouteforce procces
    print(brut_length[0], brut_length[1] + 1)
    for i in range(brut_length[0], brut_length[1] + 1):
        with open(file_name, "w") as file:
            for password in itertools.product(l, repeat=i):
                password = "".join(password)     
                
                file.write(password + '\n')
                print(password)
    print(f"file was saved with name {file_name}")

bruetforce_exel()

