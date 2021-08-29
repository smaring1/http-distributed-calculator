from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs

port = 8080
ip = '127.0.0.1'
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        url = urlparse(self.path)
        path = url.path
        query = parse_qs(url.query)

        for k in query.keys():
            query[k] = query[k][0]
        
        if (path == '/'):
            try:
                value = eval(query['exp'])
                self.send_response(200)
                self.send_header("content-type", "text/plain")
                self.end_headers()
                self.wfile.write(bytes(str(value), 'utf-8'))
            except:
                self.send_response(400)
                self.send_header("content-type", "text/plain")
                self.end_headers()
                self.wfile.write(bytes('Invalid expression\n', 'utf-8'))

        
        elif (path == '/ping'):
            self.send_response(200)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("Connection established", 'utf-8'))
        
        else:
            self.send_response(404)
            self.send_header("content-type", "text/plain")
            self.end_headers()
            self.wfile.write(bytes("404 Error: Resource %s not found" % path, 'utf-8'))


if __name__ == "__main__":
    webServer = HTTPServer((ip, port), MyServer)
    print("Server started http://%s:%s" % (ip, port))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")