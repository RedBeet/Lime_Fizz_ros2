
from rpi_lcd import LCD

class Lcd:
    def __init__(self):
        lcd = LCD()
        lcd.text(" LIME  FIZZ ", 1)
    def temperature(self, temp):
        temptxt = f'temp: {temp} C'
        lcd.text(temptxt, 2)
