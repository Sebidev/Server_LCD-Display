import netifaces as ni
import serial
import time
import sys
import io

ip = ni.ifaddresses(sys.argv[2])[ni.AF_INET][0]['addr']
loadavg = open("/proc/loadavg").readline().split(" ")[:3]
text = 'IP:', ip, loadavg

print("Serialport: ", sys.argv[1], " NIC:", sys.argv[2])
#lcddisplay = serial.Serial(sys.argv[1], baudrate=9600, bytesize=8, parity='N', stopbits=1)

time.sleep(1.5)
#lcddisplay.write(bytes(text, encoding="ascii")) 
#lcddisplay.close()
print(text)