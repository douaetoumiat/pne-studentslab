from client0 import Client
from seq0 import *
from pathlib import Path

PRACTICE = 2
EXERCISE = 6

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.67"
PORT1 = 8080
PORT2 = 8081

c1 = Client(IP, PORT1)
c2 = Client(IP, PORT2)
print(c1)
print(c2)
FRAT1 = seq_read_fasta("/home/alumnos/douae/PycharmProjects/pne-studentslab/S04/text files/Homo_sapiens_FRAT1_sequence.txt")
print(FRAT1)
number = 1
start = 0
cut = 10
while number < 11:

    bases = FRAT1[start:cut]
    print(f"Fragment{number}:{bases}")
    if number % 2 != 0:
      response = c1.talk(f"Fragment{number}:{bases}")
    else :
       response = c2.talk(f"Fragment{number}:{bases}")
    number += 1
    cut += 10
    start += 10
