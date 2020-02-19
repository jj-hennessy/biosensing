import serial
import time

# set up the serial line
ser = serial.Serial('COM5', 9600, timeout=None)

# Read and record the data
data =[]                       # empty list to store the data
for i in range(10):
    b = ser.readline()
    string_n = b.decode()
    string = string_n.rstrip()
    flt = float(string)
    data.append(flt)
    time.sleep(0.1)

print("Data: ", data)
ser.close()
