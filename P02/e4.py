from client0 import Client
from seq0 import *
from pathlib import Path


PRACTICE = 2
EXERCISE = 4

print(f"-----| Practice {PRACTICE}, Exercise {EXERCISE} |------")

IP = "212.128.255.67"
PORT = 8081


c = Client(IP, PORT)
genes = ["U5.txt","FRAT1.txt","ADA.txt"]
for i in range(len(genes)):
    bases = (seq_read_fasta("/home/alumnos/douae/PycharmProjects/pne-studentslab/S04/text files/"+genes[i]))

    response1 = c.talk(f"Sending the {genes[i]}Gene to the server...")
    response2 =  c.talk(bases)
    print(f"Response: {response1}")
    print(f"Response: {response2}")

