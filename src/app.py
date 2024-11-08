from http.server import HTTPServer
from handlers.request_handler import SimpleHTTPRequestHandler
from db.database import init_db
from config import SERVER_PORT

if __name__ == "__main__":
    init_db()  # Initialize database
    server_address = ("", SERVER_PORT)
    httpd = HTTPServer(server_address, SimpleHTTPRequestHandler)
    print(f"Server running on http://localhost:{SERVER_PORT}")
    httpd.serve_forever()