# DM-WiFi
See the image of the DM WiFi Microscope on your PC Screen using Python

camera_feed_pygame.py:

Inspired by the https://github.com/K-Francis-H/little-stars-hack/blob/main/camera_feed_pygame.py file and some other file. I used it as a base to create my own Python Script.


dm-wifi_stream.py:

What it does: See the Live-Stream of the DM WiFi Microscope in your Browser. It sets up a Server and presents a MJPG Stream to the URL: http://127.0.0.1:8081/cam.mjpg or you can also use http://127.0.0.1:8081/cam.html

How to use it: connect your device with the DM WiFi Microscope. Then run the script in a terminal window like this: python3 dm-wifi_stream.py
