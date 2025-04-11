from machine import Pin
import utime

last_time = 0
debounce_ms = 200  # adjust debounce lantency
count = 0

def pin_handler(pin):
    global last_time, count
    now = utime.ticks_ms()
    if utime.ticks_diff(now, last_time) > debounce_ms:
        last_time = now
        count += 1
        print(f"interrupt: pin is HIGH {count} times")

pin29 = Pin(28, Pin.IN, Pin.PULL_DOWN)
pin29.irq(trigger=Pin.IRQ_RISING, handler=pin_handler)

while True:
    utime.sleep(1)
