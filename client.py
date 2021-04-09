import socket
import pygame
import time

def socketInit():
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    host = '192.168.1.36'
    port = 12345
    s.connect((host,port)) #conn check?
    s.send(bytes('Client connected.','UTF-8'))
    print('Waiting for RPi to response ')
    ans = s.recv(1024).decode('UTF-8')
    print(ans)
    return s

def pygameInit():
    pygame.init()
    scrn = pygame.display.set_mode((1280, 720))
    pygame.display.set_caption('Client')
    running = True
    return scrn, running

def scrnUpdate(ans,scrn):
    font = pygame.font.SysFont("",30)
    label = font.render("ESP_1:", True, (255,255,255))
    scrn.blit(label,(0,0))
    v = font.render(ans, True, (255,255,255))
    scrn.blit(v, (label.get_width() + 5, 0))
    pygame.display.update()


s = socketInit()
scrn, running = pygameInit()
ans = '0 %'
scrnUpdate(ans,scrn);
keypress = 100
control = 0
data = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                keypress = 1
                control = 1
            elif event.key == pygame.K_s:
                keypress = 0
                control = 1
    if data == 'EXIT':
        break
        running = False
    if keypress == 1:
        reply = '1'
    elif keypress == 0:
        reply = '0'
    if control == 1:
        s.send(bytes(reply,'UTF-8'))
        data = s.recv(1024).decode('UTF-8')
        print(data)
        scrnUpdate(data,scrn)
        control = 0
    time.sleep(1)
s.close()
pygame.quit()



    