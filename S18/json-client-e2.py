import http.client
import json
import termcolor

PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)

# -- Send the request message, using the GET method. We are
# -- requesting the main page (/)
try:
    conn.request("GET", "/listusers")
except ConnectionRefusedError:
    print("ERROR! Cannot connect to the Server")
    exit()

# -- Read the response message from the server
r1 = conn.getresponse()

# -- Print the status line
print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
data1 = r1.read().decode("utf-8")

# -- Create a variable with the data,
# -- form the JSON received
people = json.loads(data1)

print("CONTENT: ")

# Print the information in the object
print()
for i in range(len(people["people"])):
        termcolor.cprint("Name: ", 'green', end="")
        print(people["people"][i]['Firstname'], people["people"][i]['Lastname'])
        termcolor.cprint("Age: ", 'green', end="")
        print(people["people"][i]['age'])

# Get the phoneNumber list
        phoneNumbers = people["people"][i]['phoneNumber']

# Print the number of elements in the list
        termcolor.cprint("Phone numbers: ", 'green', end='')
        print(len(phoneNumbers))

# Print all the numbers
        for i, dictnum in enumerate(phoneNumbers):
            termcolor.cprint("  Phone " + str(i + 1) + ": ", 'blue')

    # The element num contains 2 fields: number and type
            termcolor.cprint("\t- Type: ", 'red', end='')
            print(dictnum['type'])
            termcolor.cprint("\t- Number: ", 'red', end='')
            print(dictnum['number'])
