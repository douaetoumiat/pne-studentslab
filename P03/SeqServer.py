import socket
from Seq1 import Seq
import termcolor

PORT = 8080
IP = "127.0.0.1"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)



ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


ls.bind((IP, PORT))

ls.listen()

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()

    # -- Server stopped manually
    except KeyboardInterrupt:
        print("Server stopped by the user")

        # -- Close the listenning socket
        ls.close()

        # -- Exit!
        exit()

    # -- Execute this part if there are no errors
    else:

        print("A client has connected to the server!")
        msg_raw = cs.recv(2048)
        msg = msg_raw.decode()


        if msg != "PING":
            print("PING COMMAND!")
            s = Seq(msg)
            s.ping()
            response = s.ping()
            cs.send(response.encode())

            cs.close()
        else:
            termcolor.cprint(f"Message received: {msg}", 'green')
            response = "ECHO:" + msg
            cs.send(response.encode())

            cs.close()




