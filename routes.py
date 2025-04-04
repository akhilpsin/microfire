routes = {}

# Route Decorator
def route(path, method="GET"):
    def decorator(func):
        if path not in routes:
            routes[path] = {}
        routes[path][method] = func
        return func
    return decorator

# Example Routes
@route("/")
def home(request):
    return {"message": "Welcome to my API!"}, 200

@route("/about")
def about(request):
    return {"message": "This is a custom API framework"}, 200

@route("/data", method="POST")
def receive_data(request):
    return {"received": request["body"]}, 201

@route("/protected", method="GET")
def protected_route(request):
    return {"message": "You accessed a protected route!"}, 200
