from http.server import BaseHTTPRequestHandler, HTTPServer
from socketserver import ThreadingMixIn
import socket

class CamHandler(BaseHTTPRequestHandler):
	def do_GET(self):
		if self.path.endswith('.mjpg'):
			self.send_response(200)
			self.send_header('Content-type', 'multipart/x-mixed-replace; boundary=--jpgboundary')
			self.end_headers()
			img = b""
			with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
				s.sendto(b"JHCMD\xd0\x01", ("192.168.29.1", 20000))
				with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as r:
					r.bind(("", 10900))
					while True:
						data = r.recv(1450)
						framecount = data[0] + data[1]*256
						if data[3]==0:
							if len(img) > 0:
								self.send_header('Content-type', 'image/jpeg')
								self.send_header('Content-length', len(img))
								self.end_headers()
								self.wfile.write(img)
								self.wfile.write(b"\r\n--jpgboundary\r\n")
								img = b""
							if framecount%50 == 0:
								s.sendto(b"JHCMD\xd0\x01", ("192.168.29.1", 20000))
						img += data[8:]
			return

		if self.path.endswith('.html'):
			self.send_response(200)
			self.send_header('Content-type', 'text/html')
			self.end_headers()
			self.wfile.write(b'<html><head></head><body><img src="http://127.0.0.1:8081/cam.mjpg"/></body></html>')
			return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
	"""Handle requests in a separate thread."""

if __name__ == '__main__':
	server = ThreadedHTTPServer(('localhost', 8081), CamHandler)
	print("server started at http://127.0.0.1:8081/cam.html")
	server.serve_forever()