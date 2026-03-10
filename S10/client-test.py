from client0 import Client
IP = "212.128.255.67"
PORT = 8080
c = Client(IP, PORT)
for i in range(0,5):
    msg = "Message" + str(i)
    c.talk(msg)