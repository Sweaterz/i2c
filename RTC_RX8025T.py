import smbus
import time


def read_second():

    with smbus.SMBus(0) as bus:
        bus.write_byte(0x32, 0x00)
        # time.sleep(0.05)
        data = bus.read_i2c_block_data(0x32, 2)
        print(data)


if __name__ == '__main__':
    read_second()
