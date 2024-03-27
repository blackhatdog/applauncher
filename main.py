import serial
import subprocess as sub
import webbrowser as wb
ser = serial.Serial('COM6',115200, timeout=2, xonxoff=False, rtscts=False, dsrdtr=False,parity=serial.PARITY_NONE,stopbits=serial.STOPBITS_ONE) #Tried with and without the last 3 parameters, and also at 1Mbps, same happens.
ser.flushInput()
ser.flushOutput()
while True:
  data_raw = ser.readline()
  print(data_raw)
  if data_raw == b'first':
    #sub.Popen("C:/Program Files/Google/Chrome/Application/chrome.exe")
     wb.open("mcraft.fun")

  if data_raw == b'second':
    sub.Popen("C:/Program Files/Google/Chrome/Application/chrome.exe")
     
  else:
     print(0)