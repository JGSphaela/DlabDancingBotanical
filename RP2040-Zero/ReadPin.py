from machine import Pin

pin = Pin(28, Pin.IN)  # replace 2 with your gpio pin number

while True:
    val = pin.value()
    print("HIGH" if val else "LOW")
