from http.server import BaseHTTPRequestHandler
import json
from db import database


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def send_json(self, data, status=200):
        self.send_response(status)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode("utf-8"))

    def do_GET(self):
        users = database.get_all_users()
        self.send_json(users)

    def do_POST(self):
        content_length = int(self.headers.get("Content-Length", 0))
        post_data = self.rfile.read(content_length)
        data = json.loads(post_data.decode("utf-8"))
        user_id = database.create_user(data["name"], data["age"])
        self.send_json({"message": "User created", "id": user_id}, status=201)

    def do_DELETE(self):
        user_id = int(self.path.split("/")[-1])
        database.delete_user(user_id)
        self.send_json({"message": "User deleted"})