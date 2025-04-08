import machine, neopixel, utime
np = neopixel.NeoPixel(machine.Pin(16), 1)

sensor_pir = machine.Pin(29,machine.Pin.IN, machine.Pin.PULL_DOWN)

def pir_handler(pin):
    np[0] = (255, 0, 0)  # red
    np.write()
    utime.sleep(.5)
    np[0] = (0, 0, 0)    # off
    np.write()
    utime.sleep(.5)
    
sensor_pir.irq(trigger=machine.Pin.IRQ_RISING, handler=pir_handler)