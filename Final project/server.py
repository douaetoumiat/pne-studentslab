import http.server
import http.client
import socketserver
import termcolor
import json
from Seq1 import *
from urllib.parse import parse_qs, urlparse

# Define the Server's port
PORT = 8080


socketserver.TCPServer.allow_reuse_address = True



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

        if resource == "/":
            # Read the file
            contents = Path('html/index.html').read_text()
            content_type = 'text/html'
            error_code = 200
        elif resource == "/ListSpecies":
            SERVER = "rest.ensembl.org"
            ENDPOINT = f"/info/species"
            PARAMS = '?content-type=application/json'
            URL = SERVER + ENDPOINT + PARAMS
            conn = http.client.HTTPSConnection(SERVER)
            conn.request("GET", ENDPOINT + PARAMS)

            response = conn.getresponse()
            data = json.loads(response.read().decode())
            species = data["species"]
            number_species =  len(species)
            limit_selected = int(arguments["entered_limit"][0])
            vertebrates = [s for s in species  if s['division'] == 'EnsemblVertebrates']
            list_names = []
            text_html =f"""<!DOCTYPE html>
                        <html lang="en">
                        <head>
                            <meta charset="UTF-8">
                            <title>Species List</title>
                        </head>
                        <body  style="background-color: lightcyan;">
                        <H1 style="background-color: powderblue;">SPECIES LIST</H1>
                        <P>The number of species in the database is: {number_species}</P>
                        <p>The limit you have selected is : {limit_selected}</p>
                        <p>The list of species :</p>

                        <ul>
                                
                            
                        """
            end_html = """</ul>
                        </body>
                        </html>"""


            for i in range(limit_selected):
                list_names.append(vertebrates[i]["common_name"])

            for i in range(len(list_names)):

                name = list_names[i]
                text_html = text_html + f"<li>{name}</li>\n"

            contents = text_html + end_html
            content_type = 'text/html'
            error_code = 200
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