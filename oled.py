from machine import Pin, SPI, ADC
from time import sleep
from ssd1351 import Display, color565

def setup_display():
    #mosi=sda
    spi = SPI(2, 14500000, miso=Pin(19), mosi=Pin(18), sck=Pin(5))
    display = Display(spi, rst=Pin(26), dc=Pin(25), cs=Pin(4))
    return display

def cleanup_display(display):
    print('clearing display')
    display.clear()
    display.cleanup()

display = setup_display()


from xglcd_font import XglcdFont
font = XglcdFont('fonts/Bally7x9.c', 7, 9)

display.draw_text(40, 30, "EDC", font, color565(0, 0, 255))
display.draw_text(38, 40, "2018", font, color565(0, 0, 255))
