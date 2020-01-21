#!/usr/bin/env python3

import socket
import time

import pygame


HOST = '192.168.7.238'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)
joystick.init()
print("Joystick recognized: ")
print(joystick.get_name())
print(joystick.get_numbuttons())

servoRange = 500
stringXAxis = "xAxis "
stringYAxis = "yAxis "
stringZAxis = "zAxis "
value = " "

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:

    s.connect((HOST, PORT))

    while True:

        # value = input("Input new value: ")
        pygame.event.pump()
        joystick.get_axis(0)
        joystick.get_axis(1)
        joystick.get_axis(2)
        joystick.get_axis(3)

        xInput = joystick.get_axis(0) * servoRange
        yInput = joystick.get_axis(1) * servoRange
        zInput = joystick.get_axis(3) * servoRange

        if joystick.get_button(1) == 1:
            value = "q"

        if joystick.get_button(1) != 1:
            xData = str(xInput + 1500)
            yData = str(yInput + 1500)
            zData = str(zInput + 1500)
            value = (stringXAxis + xData + " " + stringYAxis + yData + " " + stringZAxis + zData)

        s.sendall(bytes(value, 'utf8'))

        # time.sleep(0.00166)

        data = s.recv(1024)
        # receivedData = str(data, 'utf8')
        # counter = counter + 1
        # print('Received ' + receivedData + " ", counter)