import json
import termcolor
from pathlib import Path

# -- Read the json file
jsonstring = Path("people-e1.json").read_text()

# Create the object person from the json string
people = json.loads(jsonstring)


# Print the information on the console, in colors
print(f"Total people in the database:{len(people["people"])}")
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
