import http.client
import http.server
import json
from Seq1 import *

genes = {"FRAT1": "ENSG00000165879",
         "ADA": "ENSG00000196839",
         "FXN": "ENSG00000165060",
         "RNU6_269P": "ENSG00000212379",
         "MIR633": "ENSG00000207552",
         "TTTY4C": "ENSG00000228296",
         "RBMY2YP": "ENSG00000227633",
         "FGFR3": "ENSG00000068078",
         "KDR": "ENSG00000128052",
         "ANK2": "ENSG00000145362"
         }
gene_need = input("Enter the desired gene:")
SERVER = "rest.ensembl.org"
ENDPOINT = f"/sequence/id/{genes[gene_need]}"
PARAMS = "?content-type=application/json"
URL = SERVER + ENDPOINT + PARAMS



conn = http.client.HTTPSConnection(SERVER)
conn.request ("GET", ENDPOINT + PARAMS)

response = conn.getresponse()
data = json.loads(response.read().decode())
s = Seq(data["seq"])


print(f"server:{SERVER}")
print(f"url:{URL}")
print(f"response:{response.status} {response.reason}!")
print(f"gene:{gene_need}")
print(f"description:{data["desc"]}")
print(s.count())
print(f"The most freuent base is:{s.biggest()}")