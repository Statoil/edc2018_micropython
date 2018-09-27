
https://github.com/SebastianRoll/slides_micropython


def interrupt(p):
    print("Button clicked!")
    
button.irq(trigger=Pin.IRQ_FALLING, handler=interrupt)

import machine
adc = machine.ADC(0)


import dht
d = dht.DHT22(machine.Pin(25))
d.measure()
d.temperature()


-- 
import machine
import dht
from machine import Pin

d = dht.DHT22(machine.Pin(25))

button_clicked = False

button = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)

def interrupt(p):
    button_clicked = True
    print("Click") 

button.irq(trigger=Pin.IRQ_FALLING, handler=interrupt)

while True:
  if button_clicked:
        d.measure()
        d.temperature()
        button_clicked = False


----
import machine
import dht
from machine import Pin

button = machine.Pin(27, machine.Pin.IN, machine.Pin.PULL_UP)

def interrupt(p):
    d = dht.DHT22(machine.Pin(25))
    d.measure()
    print(d.temperature())
    print(d.humidity())

button.irq(trigger=Pin.IRQ_FALLING, handler=interrupt)

---


