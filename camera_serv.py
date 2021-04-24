#!/usr/bin/env python3
import socket, sys
import pygame
from PIL import Image
import io
import base64

#Create a var for storing an IP address:
ip = "10.42.0.2"


X=320
Y=240
#Start PyGame:
pygame.init()
screen = pygame.display.set_mode((X,Y))
pygame.display.set_caption('Remote Webcam Viewer')
font = pygame.font.SysFont("Arial",14)
clock = pygame.time.Clock()
timer = 0
previousImage = ""
image = ""
size = 230400

#Main program loop:
flag = 1
while True:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      sys.exit()

##Receive data
  if timer < 1:

    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((str(ip),5003))

    data ="".encode()
    while len(data) != size:
      data = data + client_socket.recv(124000)

    #clock.tick(60)
    timer = 30
  else:
    timer -= 1
    previousImage = image

#Convert image
  try:
    image = Image.frombytes("RGB",(X,Y),data)
    image = image.resize((X,Y))
    output = image
    image = pygame.image.frombuffer(image.tobytes(),(X,Y),"RGB")
    screen.blit(image, (0, 0))
    pygame.display.flip()
    output = pygame.image.frombuffer(output.tobytes(), (X, Y), "RGB")



#I#nterupt..
  except Exception as ex:
    print(ex," ","timer: ",timer)
    image = previousImage





