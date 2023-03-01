# Copyright (C) 2021, Raffaello Bonghi <raffaello@rnext.it>
import atexit
import serial

py_serial = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
)

class Motor:

    def __init__(self, rpm):
        self._rpm = rpm
        self._leftdirection = "F"
        self._rightdirection = "F"

    def set_speed(self, rpmr, rpml):
        valuer = rpmr / self._rpm
        valuel = rpml / self._rpm
        mapped_valuer = int(255 * valuer)
        mapped_valuel = int(255 * valuel)

        speedl = min(max(abs(mapped_valuel), 0), 255)
        lvel = '0' * (3 - len(str(speedl))) + str(speedl)
        speedr = min(max(abs(mapped_valuer), 0), 255)
        rvel = '0' * (3 - len(str(speedr))) + str(speedr)   
        
        if mapped_valuel < 0:
            self._leftdirection = "B"
        else:
            self._leftdirection = "F"

        if mapped_valuer < 0:
            self._rightdirection = "B"
        else:
            self._rightdirection = "F"

        commandline = self._leftdirection + lvel + self._rightdirection + rvel
        print(commandline)
        py_serial.write(str.encode(commandline))