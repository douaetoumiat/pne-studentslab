import http.server
import http.client
import socketserver
import termcolor
import json
import jinja2 as j
from Seq1 import *
from urllib.parse import parse_qs, urlparse


# Define the Server's port
PORT = 8080


socketserver.TCPServer.allow_reuse_address = True

def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents
def get_id(name):
    species = "homo_sapiens"
    gene = name
    SERVER = "rest.ensembl.org"
    ENDPOINT = f"/lookup/symbol/{species}/{gene}?"
    PARAMS = 'content-type=application/json'
    conn = http.client.HTTPSConnection(SERVER)
    conn.request("GET", ENDPOINT + PARAMS)

    response = conn.getresponse()
    data = json.loads(response.read().decode())
    id = data["id"]
    return id


class TestHandler(http.server.BaseHTTPRequestHandler):

    def do_GET(self):



        termcolor.cprint(self.requestline, 'green')
        list_resource = self.path.split('?')
        resource = list_resource[0]
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)

        path = url_path.path
        print(path)  # we get it from here
        arguments = parse_qs(url_path.query)
        try:
            json_marker = arguments["json"][0]
        except KeyError:
            json_marker = 0
        SERVER = "rest.ensembl.org"

        if resource == "/":
            # Read the file
            contents = Path('html/index.html').read_text()
            content_type = 'text/html'
            error_code = 200
        elif resource == "/listSpecies":
            try:
                ENDPOINT = f"/info/species"
                PARAMS = '?content-type=application/json'
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)
                response = conn.getresponse()
                data = json.loads(response.read().decode())
                species = data["species"]
                if " " in species :
                    species.replace("%20")
                vertebrates = [s for s in species if s['division'] == 'EnsemblVertebrates']
                number_species =  len(species)
                limit_selected = int(arguments["limit"][0])
                print(limit_selected)
                list_names = []
                text_html = ""
                for i in range(limit_selected):
                    list_names.append(vertebrates[i]["common_name"])
                for i in range(len(list_names)):
                    name = list_names[i]
                    text_html = text_html + f"<li>{name}</li>\n"
                if json_marker == "1":
                    d = {"species list":list_names}
                    contents = json.dumps(d)
                    error_code = 200
                    content_type = 'application/json'
                else:
                    contents = read_html_file("limit_species.html").render(number_species=number_species, limit_selected=limit_selected,text_html=text_html)
                    content_type = 'text/html'
                    error_code = 200
            except KeyError:
                contents = Path('html/error.html').read_text()
                content_type = 'text/html'
                error_code = 404

        elif resource == "/karyotype":
            try:
                species = arguments['species'][0]
                if " " or "+" in species:
                    species = species.replace(" ", "%20").replace("+", "%20")
                    print(species)

                ENDPOINT =f"/info/assembly/{species}?"
                PARAMS = 'content-type=application/json'
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)

                response = conn.getresponse()
                data = json.loads(response.read().decode())
                karyotype = data["karyotype"]
                text_html = ""
                list_karyo =[]
                for i in range(len(karyotype)):
                    name = karyotype[i]
                    list_karyo.append(name)
                    text_html = text_html + f"<p>{name}</p>\n"
                if json_marker == "1":
                    d = {"species":species,"karyotype":list_karyo}
                    contents = json.dumps(d)
                    error_code = 200
                    content_type = 'application/json'
                else:
                    species_html = str(species.replace("%20"," "))
                    contents = read_html_file("karyotype.html").render(species=species_html,text_html=text_html)
                    content_type = 'text/html'
                    error_code = 200
            except KeyError:
                contents = Path('html/error.html').read_text()
                content_type = 'text/html'
                error_code = 404

        elif resource == "/chromosomeLength":
            try:
                species2 = arguments['species'][0]
                chromo = arguments['chromo'][0]

                ENDPOINT = f"/info/assembly/{species2}?"
                PARAMS = 'content-type=application/json'
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)
                ENDPOINT = f"/info/assembly/{species2}?"
                PARAMS = 'content-type=application/json'
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)
                response = conn.getresponse()
                data = json.loads(response.read().decode())
                print(data)
                dict_chrom_mix =data["top_level_region"]
                result = " "
                for i in range(len(dict_chrom_mix)):
                    if dict_chrom_mix[i]["name"] == f"{chromo}":
                        result =  dict_chrom_mix[i]["length"]
                if json_marker == "1":
                    d = {"Chromosome":chromo,"Length":result}
                    contents = json.dumps(d)
                    error_code = 200
                    content_type = 'application/json'
                else:
                    contents = read_html_file("chromo_length.html").render(chromo=chromo,result=result)
                    content_type = 'text/html'
                    error_code = 200
            except KeyError:
                contents = Path('html/error.html').read_text()
                content_type = 'text/html'
                error_code = 404
        elif resource == "/geneLookup":
            try:

                gene = arguments["gene"][0]
                id = get_id(gene)
                if json_marker == "1":
                    d = {"Gene": gene, "Id": id}
                    contents = json.dumps(d)
                    error_code = 200
                    content_type = 'application/json'
                else:
                    contents = read_html_file("gene_id.html").render(gene=gene,id=id)
                    content_type = 'text/html'
                    error_code = 200

            except KeyError:
                contents = Path('html/error.html').read_text()
                content_type = 'text/html'
                error_code = 404
        elif resource == "/geneSeq":
            try:
                gene = arguments["gene"][0]
                id = get_id(gene)
                ENDPOINT = f"/sequence/id/{id}?"
                PARAMS = 'content-type=application/json'
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)

                response = conn.getresponse()
                data = json.loads(response.read().decode())
                seq = data["seq"]
                if json_marker == "1":
                    d = {"Gene": gene, "Sequence": seq}
                    contents = json.dumps(d)
                    error_code = 200
                    content_type = 'application/json'
                else:
                    contents = read_html_file("gene_seq.html").render(seq=seq,gene=gene)
                    content_type = 'text/html'
                    error_code = 200
            except KeyError:
                contents = Path('html/error.html').read_text()
                content_type = 'text/html'
                error_code = 404
        elif resource == "/geneInfo":
            try:
                gene = arguments["gene"][0]
                id = get_id(gene)
                ENDPOINT = f"/lookup/id/{id}?"
                PARAMS = 'content-type=application/json'
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)
                response = conn.getresponse()
                data = json.loads(response.read().decode())

                start = data["start"]
                end = data["end"]
                name = data["seq_region_name"]
                length =  end - start
                if json_marker == "1":
                    d = {"Id": id, "Gene": gene,"Start":start,"End":end,"Chromosome":name,"Length":length}
                    contents = json.dumps(d)
                    error_code = 200
                    content_type = 'application/json'
                else:
                    contents = read_html_file("gene_info.html").render(id=id, gene=gene,start=start,end=end,name =name,length =length)
                    content_type = 'text/html'
                    error_code = 200
            except KeyError:
                contents = Path('html/error.html').read_text()
                content_type = 'text/html'
                error_code = 404
        elif resource == "/geneCalc":
            try:
                gene = arguments["gene"][0]
                id = get_id(gene)
                ENDPOINT = f"/sequence/id/{id}?"
                PARAMS = 'content-type=application/json'
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)

                response = conn.getresponse()
                data = json.loads(response.read().decode())
                seq = data["seq"]
                seq = Seq(seq)
                d = {"Gene": gene}

                for i in range(4):

                    info = seq.count()
                    info_s = info.splitlines()
                    info_ss = info_s[i].split(":")
                    d[info_ss[0]]=[info_ss[1]]
                if json_marker == "1":

                    j = json.dumps(d)
                    contents = j
                    error_code = 200
                    content_type = 'application/json'
                else:
                    contents = read_html_file("gene_calc.html").render(info=info, gene=gene)
                    content_type = 'text/html'
                    error_code = 200

            except KeyError:
                contents = Path('html/error.html').read_text()
                content_type = 'text/html'
                error_code = 404
        elif resource == "/geneList":
            try:
                start = arguments["start"][0]
                end = arguments["end"][0]
                chromo = arguments["chromo"][0]
                ENDPOINT = f"overlap/region/human/{chromo}:{start}-{end}?"
                PARAMS = 'content-type=application/json;feature=gene'
                conn = http.client.HTTPSConnection(SERVER)
                conn.request("GET", ENDPOINT + PARAMS)

                response = conn.getresponse()
                data = json.loads(response.read().decode())
                gene_list = []
                list_text = ""
                for i in range(len(data)):
                    if  data[i]["feature_type"] == "gene":
                        gene_list.append(data[i]["external_name"])

                for i in range(len(gene_list)):
                    name = gene_list[i]
                    list_text =list_text + f"<li>{name}</li>\n"
                if json_marker == "1":
                    d = {"Chromosome":chromo,"Human gene":gene_list}
                    j = json.dumps(d)
                    contents = j
                    error_code = 200
                    content_type = 'application/json'
                else:
                    contents = read_html_file("gene_overlap.html").render(chromo=chromo,list_text=list_text)
                    content_type = 'text/html'
                    error_code = 200

            except KeyError:
                contents = Path('html/error.html').read_text()
                content_type = 'text/html'
                error_code = 404


        else:
            contents = Path('html/error.html').read_text()
            content_type = 'text/html'
            error_code = 404

        # Generating the response message
        self.send_response(error_code)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', content_type)
        self.send_header('Content-Length', len(str.encode(contents)))

        # The header is finished
        self.end_headers()

        # Send the response message
        self.wfile.write(str.encode(contents))

        return


# ------------------------
# - Server MAIN program
# ------------------------
# -- Set the new handler
Handler = TestHandler

# -- Open the socket server
with socketserver.TCPServer(("", PORT), Handler) as httpd:

    print("Serving at PORT", PORT)

    # -- Main loop: Attend the client. Whenever there is a new
    # -- clint, the handler is called
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("")
        print("Stopped by the user")
        httpd.server_close()