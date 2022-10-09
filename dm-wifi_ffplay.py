import socket
import sys
# python3 dm-wifi_ffplay.py | ffplay -
if __name__ == '__main__':
	img = b''
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
		s.sendto(b'JHCMD\xd0\x01', ('192.168.29.1', 20000))
		with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as r:
			r.bind(('', 10900))
			while True:
				data = r.recv(1450)
				framecount = data[0] + data[1]*256
				if data[3]==0:
					if len(img) > 0:
						try:
							sys.stdout.buffer.write(img)
						except Exception as e:
							print(e)
						img = b''
					if framecount%50 == 0:
						s.sendto(b'JHCMD\xd0\x01', ('192.168.29.1', 20000))
				img += data[8:]