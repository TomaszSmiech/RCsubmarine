#!/usr/bin/env python3
# arduino check, sock check
import serial
import socket
import time

def serialInit():
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1) #serial error if wrong device
    ser.flush()
    print('Waiting for Arduino to response', end='')
    while True:
        print('.',end='')
        if ser.readline().decode('utf-8').rstrip() == 'Connected Arduino':
            print('\nArduino connected.')
            break
    return ser

def socketInit():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    host = '192.168.1.36'
    port = 12345
    print("Waiting for connection request.")
    try:
        s.bind((host, port))
    except socket.error:
        print('Bind failed')
    s.listen(1)
    c, addr = s.accept()
    print ('Got connection from',addr)
    ans = c.recv(1024).decode('UTF-8')
    print(ans)
    c.send(bytes('Connected to RPi','UTF-8'))
    return c, addr

ser = serialInit()
ser.timeout = None
c ,addr = socketInit()
ans = ser.readline().decode('utf-8').rstrip()
print(ans)

while True:
    #print('Type: EXIT to terminate.')
    #if input() == 'EXIT':
    #    break
    ans_socket = c.recv(1024).decode('UTF-8')
    #print('garim ',ans_socket,type(ans_socket))
    if ans_socket == '1':
        #print('+')
        ser.write(str(1).encode('utf-8'))
    elif ans_socket == '0':
        #print('-')
        ser.write(str(0).encode('utf-8'))
    elif ans_socket == 'EXIT':
        c.send(bytes('EXIT','UTF-8'))
        break
    print('Waiting for Arduino')
    ans_serial = ser.readline().decode('utf-8').rstrip()
    print(ans_serial)
    c.send(bytes(ans_serial,'UTF-8'))
    time.sleep(1)
#c.send(bytes('EXIT','UTF-8'))
c.close()