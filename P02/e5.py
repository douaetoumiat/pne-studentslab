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
FRAT1 = seq_read_fasta("/home/alumnos/douae/PycharmProjects/pne-studentslab/S04/text files/Homo_sapiens_FRAT1_sequence.txt")
print(FRAT1)
number = 1
start = 0
cut = 5
while number < 6:

    bases = FRAT1[start:cut]
    print(f"Fragment{number}:{bases}")
    number += 1
    cut += 5
    start += 5
