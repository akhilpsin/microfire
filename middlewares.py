middlewares = []

# Middleware Decorator
def use_middleware(func):
    middlewares.append(func)
    return func

# Authentication Middleware
@use_middleware
def auth_middleware(request):
    auth_header = request["headers"].get("Authorization")
    if not auth_header or auth_header != "auth_token_123":
        return {"error": "Unauthorized"}, 401  # Stop request if not authenticated
