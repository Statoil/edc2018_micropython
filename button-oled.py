import machine
import dht
from machine import Pin
from machine import Pin, SPI, ADC
from time import sleep
from ssd1351 import Display, color565
from xglcd_font import XglcdFont

def setup_display():
    #mosi=sda
    spi = SPI(2, 14500000, miso=Pin(19), mosi=Pin(18), sck=Pin(5))
    display = Display(spi, rst=Pin(26), dc=Pin(25), cs=Pin(4))
    return display

def cleanup_display(display):
    if display is not None:
        print('clearing display')
        display.clear()
        display.cleanup()


button = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)
display=setup_display()
d = dht.DHT22(machine.Pin(22))
font = XglcdFont('fonts/Bally7x9.c', 7, 9)

def interrupt(p):
    d.measure()
    display.clear()
    display.draw_text(40, 30, "Temp: " + str(d.temperature()), font, color565(0, 0, 255))
    display.draw_text(38, 40, "Hum: " + str(d.humidity()), font, color565(0, 0, 255))

button.irq(trigger=Pin.IRQ_FALLING, handler=interrupt)




