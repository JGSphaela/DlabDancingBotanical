
import machine, utime
from machine import Pin

servo = machine.PWM(machine.Pin(29))
servo.freq(50)

def set_angle(angle):
    angle = max(0, min(180, angle))
    min_us = 500
    max_us = 2500
    us = min_us + (max_us - min_us) * angle / 180
    duty_u16 = int(us * 65535 / 20000)  # scale to 16-bit range over 20ms
    servo.duty_u16(duty_u16)

def goto_angle(start, stop, speed): # speed: 1-100, start stop angle
    if start < stop:
        for angle in range(start, stop, 1):
            set_angle(angle)
            utime.sleep(0.3 / speed)
    else:
        for angle in range(start, stop, -1):
            set_angle(angle)
            utime.sleep(0.3 / speed)


# servo action when triggered
def move_servo():
    set_angle(0)
    utime.sleep(1)
    set_angle(180)
    utime.sleep(1)
    goto_angle(180, 90, 50)
    goto_angle(90, 45, 100)


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
        move_servo()

pin29 = Pin(28, Pin.IN, Pin.PULL_DOWN)
pin29.irq(trigger=Pin.IRQ_RISING, handler=pin_handler)

while True:
    set_angle(180) # set the default angel
    machine.idle()