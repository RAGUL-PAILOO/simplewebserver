from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<!DOCTYPE html>
<html>
    <head>
        <title>ragul</title>
    </head>
    <body>
        <h1 align="center">Register Number-25008715</h1>
        <h2 align="center">Name-Ragul</h2>
        <h3 align="center">SEMESTER MARKS</h3>
        <br>
        <center>
            <table border="3" cellspacing="5" callpading="5">

        </center>
            <tr>
                <th>S.no</th>
                <th>Subject Name</th>
                <th>Marks</th>
            </tr>

            <tr>
                <td>1</td>
                <td>Communicative English</td>
                <td>94</td>
            </tr>
            <tr>
                <td>2</td>
                <td>Fundamental of Data Science</td>
                <td>95</td>
            </tr>
            <tr>
                <td>3</td>
                <td>fundamental of Web Application Development</td>
                <td>100</td>
            </tr>
            <tr>
                <td>4</td>
                <td>Physics for Quantum Computing</td>
                <td>97</td>
            </tr>
            <tr>
                <td>5</td>
                <td>Digital ELectronics</td>
                <td>96</td>
            </tr>
    </body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()