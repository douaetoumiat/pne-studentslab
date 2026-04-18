import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse
import jinja2 as j
from Seq1 import Seq


# provide a dictionary to build the form
def read_html_file(filename):
    contents = Path("html/" + filename).read_text()
    contents = j.Template(contents)
    return contents
# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):





      def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)

        path = url_path.path
        print (path)# we get it from here
        arguments = parse_qs(url_path.query)
        print(arguments)
        # Open the form1.html file
        # Read the index from the file
        if "GET / HTTP/1.1" == self.requestline:
            contents = Path('html/index.html').read_text()
        elif path ==  "/Ping":
                contents = Path('html/ping.html').read_text()

        elif path == "/Get":
            numbers = {0:"ACT",1:"CCGT",2:"AGAT",3:"ACHT",4:"GGATC"}
            number = int(arguments["sequence"][0])
            chosen_seq = numbers[number]
            contents = read_html_file("get.html").render(sequence=chosen_seq,chosen_num=number)

        elif path == "/Gene":
            s = Seq()
            genes_dict = {0: "ADA", 1: "FRAT1", 2: "FXN", 3: "RNU6", 4: "U5"}
            number = int(arguments["genes"][0])
            chosen_gene = s.read_fasta(f"text files/{genes_dict[number]}.txt")
            contents = read_html_file("gene.html").render(Gene=chosen_gene, chosen_gene=genes_dict[number])

        elif path == "/Operation":
            seq_input = Seq(arguments["entered_seq"][0])
            operation = arguments["op"][0]
            if operation == "INFO":
                result = seq_input.count()

            elif operation == "COMP":
                result = seq_input.complement()
            elif operation == "REV":
                result = seq_input.reverse()

            contents = read_html_file("operation.html").render(sequence=seq_input, operation_type=operation,results= result)
        else:
            contents = Path('html/error.html').read_text()


        # Generating the response message
        self.send_response(200)  # -- Status line: OK!

        # Define the content-type header:
        self.send_header('Content-Type', 'text/html')
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
