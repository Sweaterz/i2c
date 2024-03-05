import smbus
import time


def detect():
    # Get I2C bus     Select Bus 0 aka i2c-0
    bus = smbus.SMBus(0)

    # BH1730 address, 0x29(41)
    # Send power on command
    #               0x10        Power On
    bus.write_byte(0x29, 0x80)
    bus.write_byte(0x29, 0x0B)

    time.sleep(0.5)

    # BH1730 address, 0x29(41)
    # Read data back, 2 bytes using General Calling
    # luminance MSB, luminance LSB
    bus.write_byte(0x29, 0x94)
    data = bus.read_i2c_block_data(0x29, 4)

    # Convert the data
    # 增益
    gain = 1
    # Integration time is determined by ITIME value
    Tint = 4 * 0.001  # 4 us = 0.004ms Max of Internal Clock Period
    ITIME = 13 * 16 + 10  # 218
    ITIME_ms = Tint * 964 * (256 - ITIME)
    data0 = data[0] + data[1] * 256
    data1 = data[2] + data[3] * 256
    # print("data0:%d" % data0)
    # print("data1:%d" % data1)
    if data0 == 0:
        print("Error: BH 1730 fail to get data.")
        return 0

    if data1 / data0 < 0.26:
        lumi = (1.290 * data0 - 2.733 * data1) / gain * 102.6 / ITIME_ms
    elif data1 / data0 < 0.55:
        lumi = (0.795 * data0 - 0.859 * data1) / gain * 102.6 / ITIME_ms
    elif data1 / data0 < 1.09:
        lumi = (0.510 * data0 - 0.345 * data1) / gain * 102.6 / ITIME_ms
    elif data1 / data0 < 2.13:
        lumi = (0.276 * data0 - 0.130 * data1) / gain * 102.6 / ITIME_ms
    else:
        lumi = 0

    # Output data to screen
    # print("Ambient Light luminance : %.2f lux" % lumi)
    return lumi


def describeLight(luminance):
    if luminance > 1300:
        print("Too Bright")
    elif 500 < luminance <= 1300:
        print("Bright")
    elif 100 < luminance <= 500:
        print("Medium")
    elif 20 < luminance <= 100:
        print("Dark")
    elif luminance < 20:
        print("Too Dark")


if __name__ == '__main__':
    while True:
        luminance = detect()
        print(luminance)
    # describeLight(luminance)