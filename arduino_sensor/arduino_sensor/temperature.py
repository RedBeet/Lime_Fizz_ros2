import serial

py_serial = serial.Serial(
    port='/dev/ttyACM0',
    baudrate=9600,
)

class ArduinoTemperature:
    def __init__(self) -> None:
        pass
    def getTemperature(self):
        if py_serial.readable():
            
            temp = float(py_serial.readline().decode)
            return temp