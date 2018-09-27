import machine
import dht
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

adcl = ADC(Pin(32))
adcl.atten(ADC.ATTN_11DB)
adcr = ADC(Pin(35))
adcr.atten(ADC.ATTN_11DB)

show_temp = True
sleep_count = 0
old_measurement = ""

while True:
    if sleep_count %  20 == 0:
        d.measure()
        if show_temp:
            measurement = "Temp: " + str(d.temperature())
        else:
            measurement = "Humidity: " + str(d.humidity())

    x_first=adcl.read()
    sleep(0.05)
    sleep_count += 1
    x_second=adcl.read()
    if x_second - x_first > 1000:
        show_temp = not show_temp
    else:
        if measurement == old_measurement:
            continue

    display.clear()
    #display.draw_text(80, 10, "EDC2018!", font, color565(0, 0, 255))
    display.draw_text(20, 30, measurement, font, color565(0, 0, 255))

    old_measurement = measurement
