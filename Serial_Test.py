import serial
ser = serial.Serial('COM3', 9600)
while True:
    line = ser.readline().decode("utf-8")
    line = [int(s) for s in line.split() if s.isdigit()][0]
    print(type(line))
    print(line)
