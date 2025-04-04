from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json

# Define routes and their handlers
routes = {}

def route(path, method="GET"):
    def decorator(func):
        if path not in routes:
            routes[path] = {}
        routes[path][method] = func
        return func
    return decorator

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        print(f"Requested GET Path: {path}")

        if path in routes and "GET" in routes[path]:
            response, status = routes[path]["GET"]()
        else:
            response, status = {"error": "Not Found"}, 404

        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def do_POST(self):
        parsed_url = urlparse(self.path)
        path = parsed_url.path

        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length).decode("utf-8")  # Read raw data

        print(f"Raw POST Data: {post_data}")  # Debugging

        try:
            data = json.loads(post_data)  # Attempt to parse JSON
        except json.JSONDecodeError:
            data = {"error": "Invalid JSON"}  # Better error handling

        print(f"Requested POST Path: {path}, Parsed Data: {data}")

        if path in routes and "POST" in routes[path]:
            response, status = routes[path]["POST"](data)
        else:
            response, status = {"error": "Not Found"}, 404

        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))



def run(server_class=HTTPServer, handler_class=SimpleHandler, port=8000):
    server_address = ("", port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}...")
    httpd.serve_forever()

# Define API routes
@route("/")
def home():
    return {"message": "Welcome to my API!"}, 200

@route("/about")
def about():
    return {"message": "This is a custom API framework"}, 200

@route("/data", method="POST")
def receive_data(data):
    return {"received": data}, 201

if __name__ == "__main__":
    run()
