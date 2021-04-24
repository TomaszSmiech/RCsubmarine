import socket,os
from PIL import *
import pygame,sys
import pygame.camera
from pygame.locals import *

#Create server:


#Start Pygame
pygame.init()
pygame.camera.init()
X=320
Y=240
size = X*Y*3
screen = pygame.display.set_mode((X,Y))
cam_list = pygame.camera.list_cameras()
cam = pygame.camera.Camera(cam_list[0],(X,Y),"RGBA")
cam.start()

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(("10.42.0.2",5003))
server.listen(5)

#Send data
while True:
    s,add = server.accept()
    print("Connected from",add)
    image = cam.get_image()
    image = pygame.transform.scale(image,(X,Y))
    screen.blit(image,(0,0))
    pygame.display.update()
    data = cam.get_raw()


    try:
        #print(data)
        s.sendall(data)

    except Exception as ex:
        print(ex)
        pass


    for event in pygame.event.get():
          if event.type == pygame.QUIT:
              cam.stop()
              pygame.quit()
              sys.exit()
