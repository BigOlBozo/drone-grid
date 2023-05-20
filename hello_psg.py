from keyboard import is_pressed as press
import os
from time import sleep
os.system('cls')
x = 0
y = 0
z = 0
position = x,y,z

def controller(x,y,z):
    if press('a'):
        x -= 1
        sleep(0.001)
        #print('left')
    if press('d'):
        x += 1
        sleep(0.001)
        #print('right')
    if press('w'):
        z += 1
        sleep(0.001)
        #print('forward')
    if press('s'):
        z -= 1
        sleep(0.001)
        #print('back')
    if press('space'):
        y += 1
        sleep(0.001)
        #print('up')
    if press('left shift'):
        y -= 1
        sleep(0.001)
        #print('down')
    if press('enter'):
        #print('Stop')
        exit()
    if x > 400:
        x = 400
    if y > 400:
        y = 400
    if z > 400:
        z = 400
    if x < -400:
        x = -400
    if y < -400:
        y = -400
    if z < -400:
        z = -400
            
    return [x,y,z]
while True:
    x,y,z = controller(x,y,z)
    print(x,y,z)
