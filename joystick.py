import machine
from machine import Pin, SPI, ADC
import time

adcl = ADC(Pin(32))
adcl.atten(ADC.ATTN_11DB)
adcr = ADC(Pin(35))
adcr.atten(ADC.ATTN_11DB) # change attentuation level 0-3.3V

while True:
    x=adcl.read()
    y=adcr.read()
    print("X:" + str(x) + ", Y: " + str(y))
    time.sleep(1)
