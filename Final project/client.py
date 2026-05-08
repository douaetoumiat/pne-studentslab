import http.client
import json


PORT = 8080
SERVER = 'localhost'

print(f"\nConnecting to server: {SERVER}:{PORT}\n")

# Connect with the server
conn = http.client.HTTPConnection(SERVER, PORT)
ENDPOINTS = ["/listSpecies?limit=11","/karyotype?species=mouse"
    ,"/chromosomeLength?species=mouse&chromo=18","/geneLookup?gene=FRAT1",
     "/geneSeq?gene=FRAT1","/geneInfo?gene=FRAT1","/geneCalc?gene=FRAT1","/geneList?chromo=9&start=22125500&end=22136000"]
for i in range(len(ENDPOINTS)):
    URL =f"{ENDPOINTS[i]}&json=1"
    try:
        conn.request("GET", URL)
    except ConnectionRefusedError:
        print("ERROR! Cannot connect to the Server")
        exit()

# -- Read the response message from the server
    r1 = conn.getresponse()

# -- Print the status line
    print(f"Response received!: {r1.status} {r1.reason}\n")

# -- Read the response's body
    data = r1.read().decode("utf-8")



    print("CONTENT: ")

# Print the information in the object
    print(data)

