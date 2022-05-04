import serial
import pyvjoy
import time
from pynput.keyboard import Key, Controller
# Enter Your Arduino Port Number
ser = serial.Serial('COM6', 9600)
keyboard = Controller()
j = pyvjoy.VJoyDevice(1)
time_delay = 0.05
# L B N A O F G P H K J
while True:
    data = ser.readline()
    print(data.decode().strip())
    if data.decode().strip() == "A":
        j.set_button(1, 1)
        time.sleep(time_delay)
        j.set_button(1, 0)
    if data.decode().strip() == "B":
        j.set_button(2, 1)
        time.sleep(time_delay)
        j.set_button(2, 0)
    if data.decode().strip() == "L":
        j.set_button(3, 0)
        time.sleep(time_delay)
        j.set_button(3, 1)
    if data.decode().strip() == "N":
        j.set_button(4, 1)
        time.sleep(time_delay)
        j.set_button(4, 0)
    if data.decode().strip() == "F":
        j.set_button(5, 1)
        time.sleep(time_delay)
        j.set_button(5, 0)
    if data.decode().strip() == "O":
        j.set_button(6, 1)
        time.sleep(time_delay)
        j.set_button(6, 0)
    if data.decode().strip() == "G":
        j.set_button(7, 1)
        time.sleep(time_delay)
        j.set_button(7, 0)
    if data.decode().strip() == "P":
        j.set_button(8, 1)
        time.sleep(time_delay)
        j.set_button(8, 0)
    if data.decode().strip() == "H":
        j.set_button(9, 1)
        time.sleep(time_delay)
        j.set_button(9, 0)
    if data.decode().strip() == "J":
        j.set_button(10, 1)
        time.sleep(time_delay)
        j.set_button(10, 0)
    if data.decode().strip() == "K":
        j.set_button(11, 1)
        time.sleep(time_delay)
        j.set_button(11, 0)
