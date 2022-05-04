import serial
import pyvjoy
import time
from pynput.keyboard import Key, Controller
# Enter Your Arduino Port Number
ser = serial.Serial('COM10', 9600)
keyboard = Controller()
j = pyvjoy.VJoyDevice(1)
time_delay = 0.05
last_pressed_key = 0
# L B N A O F G P H K J
while True:
    data = ser.readline()
    print(data.decode().strip())
    if data.decode().strip() == "A":
        j.set_button(1, 1)
        last_pressed_key = 1
    elif data.decode().strip() == "B":
        j.set_button(2, 1)
        last_pressed_key = 2
    elif data.decode().strip() == "L":
        j.set_button(3, 1)
        last_pressed_key = 3
    elif data.decode().strip() == "N":
        j.set_button(4, 1)
        last_pressed_key = 4
    elif data.decode().strip() == "F":
        j.set_button(5, 1)
        last_pressed_key = 5
    elif data.decode().strip() == "O":
        j.set_button(6, 1)
        last_pressed_key = 6
    elif data.decode().strip() == "G":
        j.set_button(7, 1)
        last_pressed_key = 7
    elif data.decode().strip() == "P":
        j.set_button(8, 1)
        last_pressed_key = 8
    elif data.decode().strip() == "H":
        j.set_button(9, 1)
        last_pressed_key = 9
    elif data.decode().strip() == "J":
        j.set_button(10, 1)
        last_pressed_key = 10
    elif data.decode().strip() == "K":
        j.set_button(11, 1)
        last_pressed_key = 11
    else:
        if(last_pressed_key != 0):
            j.set_button(last_pressed_key, 0)
            last_pressed_key = 0
