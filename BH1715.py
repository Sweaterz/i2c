import smbus
import time

def detect():

    # Get I2C bus
    bus = smbus.SMBus(0)

    # BH1715 address, 0x23(35)
    # Send power on command
    #               0x10(01)        Power On
    bus.write_byte(0x23, 0x01)

    # BH1715 address, 0x23(35)
    # Send continuous measurement command
    #               0x10(16)        Set Continuous high resolution mode, 1 lux resolution, Time = 120ms
    # bus.write_byte(0x23, 0x10)

    # BH1715 address, 0x23(35)
    # Send continuous measurement command
    #               0x20(32)        Set One time high resolution mode,
    bus.write_byte(0x23, 0x20)

    time.sleep(0.5)

    # BH1715 address, 0x23(35)
    # Read data back, 2 bytes using General Calling
    # luminance MSB, luminance LSB
    data = bus.read_i2c_block_data(0x23, 2)

    # Convert the data
    lumi = (data[0] * 256 + data[1]) / 1.2

    # Output data to screen
    # print("Ambient Light luminance : %.2f lux" %lumi)
    return lumi


if __name__ == '__main__':
    while True:
        luminance = detect()
        print(luminance)
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
