import serial
import time

lcddisplay = serial.Serial('COM3', baudrate=9600, bytesize=8, parity='N', stopbits=1)

text1 = 'hello world!1234567890'

time.sleep(3)

lcddisplay.write(bytes(text1, encoding="ascii")) 
lcddisplay.close()
print(text1)