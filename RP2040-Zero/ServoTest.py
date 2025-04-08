import machine, utime

servo = machine.PWM(machine.Pin(29))
servo.freq(50)

def set_angle(angle):
    angle = max(0, min(180, angle))
    min_us = 500
    max_us = 2500
    us = min_us + (max_us - min_us) * angle / 180
    duty_u16 = int(us * 65535 / 20000)  # scale to 16-bit range over 20ms
    servo.duty_u16(duty_u16)

while True:
    for angle in range(0, 181, 1):
        set_angle(angle)
        utime.sleep(0.005)
    for angle in range(180, -1, -1):
        set_angle(angle)
        utime.sleep(0.005)
