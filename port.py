#for python 2
#from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
#for python 3
from http.server import BaseHTTPRequestHandler, HTTPServer

import ssl


def p():
    content='test'
    return content

class S(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write(p())
        print('do_GET')

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):
        self._set_headers()
        #print "in post method"
        #self.data_string = self.rfile.read(int(self.headers['Content-Length']))

        #self.send_response(200)
        #self.end_headers()
        self.wfile.write(p())
#        data = simplejson.loads(self.data_string)
#        with open("test123456.json", "w") as outfile:
#            simplejson.dump(data, outfile)
#        print "{}".format(data)
#        f = open("for_presen.py")
#        self.wfile.write(f.read())
        return


def run(server_class=HTTPServer, handler_class=S, port=9453):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    httpd.socket = ssl.wrap_socket (httpd.socket,
                      keyfile='/etc/apache2/ssl/private.key',
                      certfile='/etc/apache2/ssl/certificate.crt',
                      ca_certs='/etc/apache2/ssl/ca_bundle.crt',
                      server_side=True)
    print('Starting httpd...')
    httpd.serve_forever()

if __name__ == "__main__":
    from sys import argv

if len(argv) == 2:
    run(port=int(argv[1]))
else:
    run()

