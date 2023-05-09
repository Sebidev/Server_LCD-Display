import netifaces as ni
import argparse
import serial
import time
import io

parser = argparse.ArgumentParser()
parser.add_argument("-sp", "--serialport", required=True)
parser.add_argument("-n", "--nic", required=True)
args = parser.parse_args()

print("Serialport: ", args.serialport, " NIC:", args.nic)

ip = ni.ifaddresses(args.nic)[ni.AF_INET][0]['addr']
loadavg = open("/proc/loadavg").readline().split(" ")[:3]

text = 'IP:', ip, loadavg

#lcddisplay = serial.Serial(serialport, baudrate=9600, bytesize=8, parity='N', stopbits=1)
#time.sleep(1.5)
#lcddisplay.write(bytes(text, encoding="ascii")) 
#lcddisplay.close()
print(text)