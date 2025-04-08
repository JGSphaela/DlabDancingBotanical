import machine, utime

sensor_temp = machine.ADC(4)  # channel 4 is internal temp sensor
conversion_factor = 3.3 / 65535

while True:
    reading = sensor_temp.read_u16()  # 16-bit raw adc value
    voltage = reading * conversion_factor
    temperature_c = 27 - (voltage - 0.706)/0.001721  # from datasheet
    print("Temp: {:.2f} C".format(temperature_c))
    utime.sleep(2)
