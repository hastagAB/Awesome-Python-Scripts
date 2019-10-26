#python version 3 or above

import serial
import time
import subprocess

serial_port = '/dev/ttyACM0'
baud_rate = 9600

while 1:
    ser = serial.Serial(serial_port, baud_rate)
    if (ser.readline().decode("utf-8").split()[1] == "0.010"):
        print("Waiting for data..")
        continue
    print(ser.readline().decode("utf-8").split()[1])
    tic = time.time()
    t = time.localtime()
    timestamp = time.strftime("%b_%d_%Y_%H%M", t)
    filename = ("Inputfiles/"+timestamp + ".txt")

    output_file = open(filename, "w+")
    output_file.write("Current\tVoltage (V)\tPower\n")
    h = 0
    while True:
        line = ser.readline()
        line = line.decode("utf-8")                 #ser.readline returns a binary, convert to string
        print(line)
        output_file.write(line)
        toc = time.time()
        # print("timestamp: ", end="")
        print(line.split()[-2])
        if line.split()[-2] == "0.010":
            h+=1
            if h ==10:
                break
    output_file.close()
    subprocess.call(" python test.py", shell=True)
    print("Predicted!")
