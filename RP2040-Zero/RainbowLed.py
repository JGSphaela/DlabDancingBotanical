import machine, neopixel, utime
np = neopixel.NeoPixel(machine.Pin(16), 1)

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

hue = 0.0
brightness = 1
index = 1
while True:
    rgb = hsv_to_rgb(hue, 1.0, brightness * 0.01)  # adjust brightness here (v=0.2)
    np[0] = rgb
    np.write()
    hue += 0.01
    if hue >= 1.0:
        hue = 0.0
    if brightness >= 20:
        index = -1
    elif brightness <= 0:
        index = 1
    brightness += index
    utime.sleep(0.05)

