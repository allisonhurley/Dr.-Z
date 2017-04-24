import serial
import time
ser = serial.Serial('COM8', 115200, timeout = 1)
ser.write("LANE_0\n")
