import socket
import termcolor

# Configure the Server's IP and PORT
PORT = 8080
IP = "212.128.255.67"
ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)


ls = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# -- Optional: This is for avoiding the problem of Port already in use
ls.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# -- Step 2: Bind the socket to server's IP and PORT
ls.bind((IP, PORT))

# -- Step 3: Configure the socket for listening
ls.listen()
connection = 0
clients = []

print("The server is configured!")

while True:
    # -- Waits for a client to connect
    print("Waiting for Clients to connect")

    try:
        (cs, client_ip_port) = ls.accept()
        clients.append(client_ip_port)
        connection += 1

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

        # -- Read the message from the client
        # -- The received message is in raw bytes
        msg_raw = cs.recv(2048)

        # -- We decode it for converting it
        # -- into a human-redeable string
        msg = msg_raw.decode()

        # -- Print the received message
        termcolor.cprint(f"Message received: {msg}", 'green')
        print("Connection:",connection,"Client(IP,PORT):",client_ip_port)
        response = "ECHO:" + msg

        # -- The message has to be encoded into bytes
        cs.send(response.encode())

        # -- Send a response message to the client


        # -- Close the data socket
        cs.close()
        if connection >= 5:
            for i in range(len(clients)):
                print(f"Client {i + 1}: {clients[i]}")

                ls.close()


