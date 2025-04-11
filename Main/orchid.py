import neopixel, utime
from machine import Pin

np = neopixel.NeoPixel(Pin(16), 1)
black_light_pin = Pin(29, Pin.OUT, Pin.PULL_DOWN)
black_light_pin.off()

    
def hsv_to_rgb(h, s, v):
    h = float(h)
    s = float(s)
    v = float(v)
    if s == 0.0: return (int(v*255),) * 3
    i = int(h*6.)  # assume h in [0,1)
    f = (h*6.) - i
    p = v*(1.-s)
    q = v*(1.-s*f)
    t = v*(1.-s*(1.-f))
    i = i%6
    if i == 0: r, g, b = v, t, p
    elif i == 1: r, g, b = q, v, p
    elif i == 2: r, g, b = p, v, t
    elif i == 3: r, g, b = p, q, v
    elif i == 4: r, g, b = t, p, v
    elif i == 5: r, g, b = v, p, q
    return int(r*255), int(g*255), int(b*255)

brightness = 1
index = 1

def loop_default(): # idle animation
    global brightness
    global index

    # idle H, S, V
    idle_hue = 24
    idle_sat = 15
    idle_vel = 10
    
    hue = idle_hue / 360
    sat = idle_sat / 100
    rgb = hsv_to_rgb(hue, sat, brightness * 0.0001 * idle_vel) 
    np[0] = rgb
    np.write()
    # hue += 0.01
    # if hue >= 1.0:
    #     hue = 0.0

    if brightness >= 100:
        index = -1
    elif brightness <= 0:
        index = 1
    brightness += index
    utime.sleep(0.05)

def trigger_animation():
    trigger_hs = ((344, 80), (0, 80), (0, 0)) # H, S value when triggered, in sets
    duration = 1 # duration of every color, in second

    black_light_pin.on()
    for hue, sat in trigger_hs:
        brightness = 1
        index = 1
        print(f'hue: {hue}, sat: {sat}')
        while True:
            if brightness >= 100:
                index = -1
            elif brightness <= 0:
                break

            brightness += index
            rgb = hsv_to_rgb(hue / 360, sat * 0.01, brightness * 0.01)
            np[0] = rgb
            np.write()
            utime.sleep(duration / 100)

    black_light_pin.off()

        
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
        trigger_animation()
        

pin29 = Pin(28, Pin.IN, Pin.PULL_DOWN)
pin29.irq(trigger=Pin.IRQ_RISING, handler=pin_handler)



while True:
    loop_default()