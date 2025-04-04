# MicroFire - A Simple Custom API Framework in Python

MicroFire is a lightweight and customizable Python framework for building APIs. It provides a basic server setup, route handling, middleware support, and a simple way to define and manage routes for your application.

## Features
- **Custom Routing**: Easily define routes and associate them with functions.
- **Middleware Support**: Attach middleware functions for authentication, logging, or custom processing.
- **Request Handling**: Supports GET and POST requests.
- **Extensible**: Easily add more routes or middleware as needed.

## Project Structure

```
microfire/
├── server.py          # Main entry point to start the server.
├── handler.py         # Handles HTTP requests and integrates middleware.
├── routes.py          # Defines all API routes and their handlers.
├── middlewares.py     # Contains middleware logic (e.g., authentication).
└── README.md          # This documentation file.
```

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/microfire.git
   cd microfire
   ```

2. Ensure you have Python 3.x installed.

3. Install required dependencies (optional):
   - Currently, the project doesn't require any external dependencies, but you can manage it using `requirements.txt` for any future dependencies.

## Running the API Server

1. Navigate to the project directory:
   ```bash
   cd microfire
   ```

2. Run the server:
   ```bash
   python server.py
   ```

   This will start the server on `http://localhost:8000`.

3. Test your API using `curl` or Postman.

   Example:
   ```bash
   # Home route
   curl -X GET http://localhost:8000/
   
   # Protected route (without token)
   curl -X GET http://localhost:8000/protected
   
   # Protected route (with token)
   curl -X GET http://localhost:8000/protected -H "Authorization: auth_token_123"
   ```

## Routes

### `GET /`
- **Description**: Returns a welcome message.
- **Response**:
  ```json
  { "message": "Welcome to my API!" }
  ```

### `GET /about`
- **Description**: Returns information about the framework.
- **Response**:
  ```json
  { "message": "This is a custom API framework" }
  ```

### `POST /data`
- **Description**: Accepts data in the request body and returns it.
- **Request**:
  ```json
  { "name": "John" }
  ```
- **Response**:
  ```json
  { "received": { "name": "John" } }
  ```

### `GET /protected`
- **Description**: A protected route that requires authentication.
- **Authentication**: Pass `Authorization: auth_token_123` header to access.
- **Response**:
  ```json
  { "message": "You accessed a protected route!" }
  ```

## Middleware

### Authentication Middleware

The API includes a simple authentication middleware that checks for the `Authorization` header in the request. If the header does not match `auth_token_123`, the request is denied with a 401 Unauthorized error.

## Contributing

Feel free to fork the repository, create a branch, and submit pull requests. Contributions are welcome!

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```