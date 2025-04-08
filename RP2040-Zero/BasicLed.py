import machine, neopixel, utime
np = neopixel.NeoPixel(machine.Pin(16), 1)
while True:
    np[0] = (255, 0, 0)  # red
    np.write()
    utime.sleep(1)
    np[0] = (0, 0, 0)    # off
    np.write()
    utime.sleep(1)
