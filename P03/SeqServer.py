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

print("The seq server is configured!")

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
        msg = str(msg.upper().strip())

        if msg == "PING":
            print("PING COMMAND!")
            s = Seq()
            response = s.ping()
            print(response)
            cs.send(response.encode())

            cs.close()
        elif  msg[0:3] == "GET":
            termcolor.cprint(f" {msg[0:3]}", 'green')
            sequences = ["ACGCTA","CCGATGC","AACGTAC","GGCATTC"]
            for i in range(len(sequences)):
                number = i
                number_str = str(number)
                if msg[-1] == number_str :
                    print(sequences[i])
                    response = str(sequences[i]) + "\n"
                    cs.send(response.encode())

                    cs.close()
        elif msg[0:4] == "INFO":
            termcolor.cprint(f" {msg[0:4]}", 'green')
            sequence = msg[4:].upper().strip()
            seq = Seq(sequence)
            bases = seq.count()
            response1 = f"sequence:{ sequence} \n Total lentgh:{seq.len()} \n  "
            response2 =



        else:
            termcolor.cprint(f"Message received: {msg}", 'green')
            response = "ECHO:" + msg
            cs.send(response.encode())

            cs.close()




