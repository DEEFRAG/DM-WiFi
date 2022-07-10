from PIL import Image
import io
import pygame
import socket

def pil_img_to_surface(pil_image):
	return pygame.image.fromstring(pil_image.tobytes(), pil_image.size, pil_image.mode).convert()

if __name__ == '__main__':
	img = b""
	pygame.init()
	screen = pygame.display.set_mode((640,480))
	with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
		s.sendto(b"JHCMD\xd0\x01", ("192.168.29.1", 20000))
		with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as r:
			r.bind(("", 10900))
			while True:
				data = r.recv(1450)
				framecount = data[0] + data[1]*256
				if data[3]==0:
					if len(img) > 0:
						try:
							screen.blit(pil_img_to_surface(Image.open(io.BytesIO(bytes(img[:])))), (0,0))
							pygame.display.flip()
						except Exception as e:
							print(e)
						img = b""
					if framecount%50 == 0:
						s.sendto(b"JHCMD\xd0\x01", ("192.168.29.1", 20000))
				img += data[8:]