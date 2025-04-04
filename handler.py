from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse
import json
from routes import routes
from middlewares import middlewares

class SimpleHandler(BaseHTTPRequestHandler):

    def handle_request(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        content_length = int(self.headers.get("Content-Length", 0))
        request_body = self.rfile.read(content_length).decode("utf-8") if content_length > 0 else "{}"

        try:
            request_data = json.loads(request_body)
        except json.JSONDecodeError:
            request_data = {}

        request = {"path": path, "headers": self.headers, "body": request_data}

        # Run Middleware before handling request
        for middleware in middlewares:
            result = middleware(request)
            if result:  # If middleware returns an error, stop processing
                self.send_response(result[1])
                self.send_header("Content-Type", "application/json")
                self.end_headers()
                self.wfile.write(json.dumps(result[0]).encode("utf-8"))
                return

        # Route handling
        if path in routes and self.command in routes[path]:
            response, status = routes[path][self.command](request)
        else:
            response, status = {"error": "Not Found"}, 404

        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def do_GET(self):
        self.handle_request()

    def do_POST(self):
        self.handle_request()
