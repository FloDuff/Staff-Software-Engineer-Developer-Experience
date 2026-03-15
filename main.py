from enum import Enum
from http.server import BaseHTTPRequestHandler, HTTPServer
import threading

class ResultStack(Enum):
    STANDARD = "STANDARD"
    SPECIAL = "SPECIAL"
    REJECTED = "REJECTED"

def sort(width, height, length, mass):
    """
    Evaluates package dimensions and mass to determine dispatch stack.
    """
    volume = width * height * length
    is_bulky = volume >= 1000000 or any(dim >= 150 for dim in [width, height, length])
    is_heavy = mass >= 20

    if is_bulky and is_heavy:
        return ResultStack.REJECTED
    if is_bulky or is_heavy:
        return ResultStack.SPECIAL
    return ResultStack.STANDARD

class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"OK")

    def log_message(self, format, *args):
        pass

if __name__ == "__main__":
    print("--- Smarter Technology Dispatcher ---")
    sample = sort(200, 200, 200, 50)
    print(f"Test Case [200x200x200, 50kg]: {sample.value}")
    print("Run 'python -m unittest discover tests' for full validation.")

    server = HTTPServer(("0.0.0.0", 5000), HealthHandler)
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    print("Health check server running on port 5000")
    server.serve_forever()
