import http.server
import socketserver
import termcolor
from pathlib import Path
from urllib.parse import parse_qs, urlparse


# Define the Server's port
PORT = 8080


# -- This is for preventing the error: "Port already in use"
socketserver.TCPServer.allow_reuse_address = True


# Class with our Handler. It is a called derived from BaseHTTPRequestHandler
# It means that our class inherits all his methods and properties
class TestHandler(http.server.BaseHTTPRequestHandler):


      # provide a dictionary to build the form

    def do_GET(self):
        """This method is called whenever the client invokes the GET method
        in the HTTP protocol request"""

        # Print the request line
        termcolor.cprint(self.requestline, 'green')
        url_path = urlparse(self.path)

        path = url_path.path  # we get it from here
        arguments = parse_qs(url_path.query)
        print(arguments)
        # Open the form1.html file
        # Read the index from the file
        if "GET / HTTP/1.1" == self.requestline:
            contents = Path('html/form-e2.html').read_text()
        elif "GET /echo?" == self.requestline[0:10]:
            if arguments["chk"][0] == "on" :
                contents =f"""<!DOCTYPE html>
                        <html lang="en">
                        <head>
                        <meta charset="utf-8">
                        <title> ECHO FORM </title>
                        </head>
                        <body>
                        <p>{(arguments["msg"][0]).upper()}</p>
                        <a href="http://127.0.0.1:8080">Main page</a>
                        </form>
                        </body>
                        </html>"""
            else:
                contents = f"""<!DOCTYPE html>
                                        <html lang="en">
                                        <head>
                                        <meta charset="utf-8">
                                        <title> ECHO FORM </title>
                                        </head>
                                        <body>
                                        <p>{(arguments["msg"][0])}</p>
                                        <a href="http://127.0.0.1:8080">Main page</a>
                                        </form>
                                        </body>
                                        </html>"""
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
