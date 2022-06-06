import time
import serial

con = serial.Serial(port='/dev/ttyACM0', baudrate = 9600)
val = "0"
rx = 0
ry = 0

while 1:
    x = con.read()

    if x == "b''":
        continue
    elif x == b'\r' or x == b'\n':
        if val != "":
            v = int(val)
            if v >= 41:
                ry = v - 41
            else:
                rx = v
        val = ""
    else:
        val += str(int(x,16))




        x = con.read()
        if x == "b''":
            continue
        elif x == b'\r' or x == b'\n':
            if val != "":
                v = int(val)
                if v >= 41:
                    ty = (((v - 41)/40)*20)-15
                else:
                    tx = ((v/40)*20)-10
            val = ""
        else:
            val += str(int(x,16))
