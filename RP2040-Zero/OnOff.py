import machine, utime

ppin = machine.Pin(29, machine.Pin.OUT, machine.Pin.PULL_UP)

while True:
    ppin.on()
    utime.sleep(1)
    ppin.off()
    utime.sleep(1)