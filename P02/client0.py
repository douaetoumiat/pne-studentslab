from pathlib import Path
import socket
class Client:
    def __init__(self,ip,port):
        self.Ip = ip
        self.Port = port

    def __str__(self):
       return f"Connection to SERVER at {self.Ip } PORT: { self.Port}"
    def ping(self):
        print("OK")

    def talk(self,msg):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.Ip, self.Port))
        s.send(str.encode(msg))
        response  = s.recv(2048).decode("utf-8")
        s.close()
        return response
