import socket

# Configure the Server's IP and PORT
PORT = 8081
IP = "212.128.255.64" # it depends on the machine the server is running
flag = True
while True:
       message = input("Write a message")
       if message != "STOP":
           s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
           s.connect(IP,PORT)
           s.send(str,encode(message))
           s.close()
       else:
            flag =False


while True:
  # -- Ask the user for the message

  # -- Create the socket

  # -- Establish the connection to the Server

  # -- Send the user message

  # -- Close the socket
