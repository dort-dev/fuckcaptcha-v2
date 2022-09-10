import sys
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from fuckcaptcha import solver_task

proxy_iter = open("proxies.txt", 'r').read().rstrip().splitlines()


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        solved = solver_task.solve("B7D8911C-5CC8-A9A3-35B0-554ACEE604DA",
                                     "https://iframe.arkoselabs.com", proxy_iter)
        sys.stdout.write(f"-> Task Finished: {solved.split('|')[0]}\n")
        sys.stdout.flush()
        self.wfile.write(bytes(solved, 'utf-8'))

    def log_message(self, fmt, *args):
        # Suppress connection logs
        pass


class ThreadingSimpleServer(ThreadingMixIn, HTTPServer):
    pass


if __name__ == '__main__':
    server = ThreadingSimpleServer(('0.0.0.0', 1338), Handler)
    server.serve_forever()
