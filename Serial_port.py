import sys
import re #regular expression
import serial
#Serial takes two parameters: serial device and baudrate
ser = serial.Serial('COM5', 9600) # serial port | Baud rate
while True:
  data = ser.readline() 
  data = data.replace(b'\n', b'').replace(b'\r', b'') # format string
  print(str(data,'utf-8')) #utf-8 string