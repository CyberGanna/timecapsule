import http.server, functools
class H(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, '.html': 'text/html; charset=utf-8', '.js': 'text/javascript; charset=utf-8'}
    def log_message(self, *a): pass
http.server.ThreadingHTTPServer(('127.0.0.1', 8765), functools.partial(H, directory=__import__('os').path.join(__import__('os').path.dirname(__import__('os').path.abspath(__file__)),'../..'))).serve_forever()
