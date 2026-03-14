import socket
from client0 import Client
print("-----| Practice 3, Exercise 7 |------")
IP = "127.0.0.1"
PORT = 8080
c = Client(IP, PORT)
print("Testing PING")
print(c.talk("PING"))
print("Testing GET:")
numbers = ["0","1","2","3"]
for i in range(len(numbers)):
    msg =  "GET " + numbers[i]
    print(msg + c.talk(msg))
print("Testing INFO:")
print(c.talk("INFO ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"))
print("Testing COMP:")
print("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(c.talk("COMP ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"))
print("Testing REV:")
print("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA")
print(c.talk("REV ACCTCCTCTCCAGCAATGCCAACCCCAGTCCAGGCCCCCATCCGCCCAGGATCTCGATCA"))
print("Testing GENE:")
genes = ["U5","ADA","FXN","FRAT1","RNU6"]
for i in range(len(genes)):
    msg = "GENE " + genes[i]
    print(msg)
    print(c.talk(msg))