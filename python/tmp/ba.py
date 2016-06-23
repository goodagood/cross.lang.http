
import http.server as hs
import socketserver
import time


HOST = 'localhost'
PORT = 9000

#Handler = hs.SimpleHTTPRequestHandler

#httpd = socketserver.TCPServer(("", PORT), Handler)

#print("serving at port", PORT)
#httpd.serve_forever()

class MyHandler(hs.BaseHTTPRequestHandler):
    def do_HEAD(s):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
    def do_GET(s):
        """Respond to a GET request."""
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write("<html><head><title>Title goes here.</title></head>")
        s.wfile.write("<body><p>This is a test.</p>")
        # If someone went to "http://something.somewhere.net/foo/bar/",
        # then s.path equals "/foo/bar/".
        s.wfile.write("<p>You accessed path: %s</p>" % s.path)
        s.wfile.write("</body></html>")



def run(server_class=hs.HTTPServer, handler_class=hs.BaseHTTPRequestHandler):
    server_address = ('', PORT)
    #httpd = server_class(server_address, handler_class)
    httpd = server_class(server_address, MyHandler)


    print(time.asctime(), "Server Starts - %s:%s" % ('', PORT))
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % ('', PORT))


    #httpd.serve_forever()



run()


