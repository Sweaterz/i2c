import smbus
import os
import time
import datetime


def hex2BCD(hexNum):
    if 0 <= hexNum <= 255:
        return hexNum // 16 * 10 + hexNum % 16
    else:
        return -1


def int2BCD(intNum):
    if 0 <= intNum <= 99:
        return intNum // 10 * 16 + intNum % 10
    else:
        return -1


def readTime():
    # I2C总线0是默认的
    bus = smbus.SMBus(0)

    # I2C设备地址
    DEVICE_ADDRESS = 0x32  # 设备的I2C地址

    # 寄存器地址
    REGISTER_ADDRESSES = [0x00, 0x01, 0x02, 0x04, 0x05, 0x06]  # 要读取的寄存器地址
    date = []
    # 读取寄存器的值
    for reg_addr in REGISTER_ADDRESSES:
        try:
            value = bus.read_byte_data(DEVICE_ADDRESS, reg_addr)
            date.append(value)
            # print(f"Register 0x{reg_addr:02X} value: 0x{value:02X}")
        except Exception as e:
            print(f"Error accessing 0x{DEVICE_ADDRESS:02X}: {e}")

    # 关闭I2C通信
    bus.close()
    for i, item in enumerate(date):
        date[i] = hex2BCD(item)
    print(f"read 20{date[5]:02}-{date[4]:02}-{date[3]:02} {date[2]:02}:{date[1]:02}:{date[0]:02} from register.")
    return date


def writeTime():
    # I2C总线0是默认的
    bus = smbus.SMBus(0)

    # I2C设备地址
    DEVICE_ADDRESS = 0x32  # 设备的I2C地址

    # 寄存器地址
    REGISTER_ADDRESSES = [0x00, 0x01, 0x02, 0x04, 0x05, 0x06]  # 要读取的寄存器地址
    stringDate = ["second", "minute", "hour", "dayOfMonth", "month", "year"]
    date = []
    for i in range(6):
        tempValue = int(input("please input " + stringDate[i] + ":"))
        if stringDate[i] == "year":
            tempValue = tempValue % 2000
        date.append(int2BCD(tempValue))

    # date = [second, minute, hour, dayOfMonth, month, year]
    # 寄存器的值
    for i, reg_addr in enumerate(REGISTER_ADDRESSES):
        try:
            value = bus.write_byte_data(DEVICE_ADDRESS, reg_addr, date[i])
        except Exception as e:
            print(f"Error accessing 0x{DEVICE_ADDRESS:02X}: {e}")

    # 关闭I2C通信
    bus.close()
    print(f"have writen 20{date[5]:02}-{date[4]:02}-{date[3]:02} {date[2]:02}:{date[1]:02}:{date[0]:02} to register.")
    return date


def setSysTime(date_str):
    date = datetime.datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(date.timetuple())
    os.system('sudo date -s @"{:.0f}"'.format(timestamp))


def hcToSys():
    date = readTime()
    date_str = f"20{date[5]:02}-{date[4]:02}-{date[3]:02} {date[2]:02}:{date[1]:02}:{date[0]:02}"
    setSysTime(date_str)


if __name__ == "__main__":
    writeTime()
