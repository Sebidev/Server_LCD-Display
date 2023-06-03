import netifaces as ni
import argparse
import serial
import time
import io

parser = argparse.ArgumentParser()
parser.add_argument("-sp", "--serialport", required=True)
parser.add_argument("-n", "--nic", required=False, default="lo")
parser.add_argument("-m", "--message", required=False)
args = parser.parse_args()

ip = ni.ifaddresses(args.nic)[ni.AF_INET][0]['addr']
loadavg = open("/proc/loadavg").readline().split(" ")[:3]

output = '{}  {}'.format(ip, ' '.join(loadavg))

if args.message:
    output = args.message

lcddisplay = serial.Serial(args.serialport, baudrate=9600, bytesize=8, parity='N', stopbits=1)
time.sleep(3)
lcddisplay.write(bytes(str(output), encoding="ascii"))
time.sleep(3)
lcddisplay.close()

print(output)