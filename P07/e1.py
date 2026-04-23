import http.client
import http.server
import json

SERVER = "rest.ensembl.org"
ENDPOINT = "/info/ping"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS

conn = http.client.HTTPSConnection(SERVER)
conn.request ("GET", ENDPOINT + PARAMS)

response = conn.getresponse()
data = json.loads(response.read().decode())

print(f"server:{SERVER}")
print(f"url:{URL}")
print(f"response:{response.status} {response.reason}!")
if data["ping"] == 1:
    print("ALIVE!")