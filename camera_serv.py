import socket,sys
import pygame
from PIL import Image

#Create a var for storing an IP address:
ip = "10.42.0.2"
#Start PyGame:
pygame.init()
screen = pygame.display.set_mode((320,240))
pygame.display.set_caption('Remote Webcam Viewer')
font = pygame.font.SysFont("Arial",14)
clock = pygame.time.Clock()
timer = 0
previousImage = ""
image = ""

#Main program loop:
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

#Receive data
  if timer < 1:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
