from client0 import Client
from seq0 import *
from pathlib import Path

PRACTICE = 2
EXERCISE = 5

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.67"
PORT = 8081


c = Client(IP, PORT)
print(c)
FRAT1 = seq_read_fasta("/S04/text files/FRAT1.txt")
print(FRAT1)
number = 1
start = 0
cut = 10
while number < 6:

    bases = FRAT1[start:cut]
    print(f"Fragment{number}:{bases}")
    response = c.talk(bases)
    number += 1
    cut += 10
    start += 10
