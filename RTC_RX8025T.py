import smbus
import os
import time
from datetime import datetime


# 数据转换：  hex --> BCD  用于读取数据
def hex2BCD(hexNum):
    if 0 <= hexNum <= 255:
        return hexNum // 16 * 10 + hexNum % 16
    else:
        return -1


# 数据转换：int --> BCD 用于写入数据
def int2BCD(intNum):
    if 0 <= intNum <= 99:
        return intNum // 10 * 16 + intNum % 10
    else:
        return -1


# 读取RX8025的时间
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


# 写入时间到RX8025
def writeTime(date = []):
    # I2C总线0是默认的
    bus = smbus.SMBus(0)

    # I2C设备地址
    DEVICE_ADDRESS = 0x32  # 设备的I2C地址

    # 寄存器地址
    REGISTER_ADDRESSES = [0x00, 0x01, 0x02, 0x04, 0x05, 0x06]  # 要读取的寄存器地址
    stringDate = ["second", "minute", "hour", "dayOfMonth", "month", "year"]

    # 如果date的长度等于0那么要进行赋值（只在alpha版本使用）
    if len(date) == 0:
        for i in range(6):
            tempValue = int(input("please input " + stringDate[i] + ":"))
            if stringDate[i] == "year":
                tempValue = tempValue % 2000
            date.append(int2BCD(tempValue))
    else:
        for i in range(6):
            # 如果是年则需要对2000取余
            if i == 5:
                date[i] = int2BCD(date[i] % 2000)
            else:
                date[i] = int2BCD(date[i])
            

    # date = [second, minute, hour, dayOfMonth, month, year]
    # 寄存器的值
    for i, reg_addr in enumerate(REGISTER_ADDRESSES):
        try:
            value = bus.write_byte_data(DEVICE_ADDRESS, reg_addr, date[i])
        except Exception as e:
            print(f"Error accessing 0x{DEVICE_ADDRESS:02X}: {e}")

    # 关闭I2C通信
    bus.close()
    print(f"have writen 20{date[5]:02X}-{date[4]:02X}-{date[3]:02X} {date[2]:02X}:{date[1]:02X}:{date[0]:02X} to register.")
    return date


# 设定系统时间
def setSysTime(date_str):
    date = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
    timestamp = time.mktime(date.timetuple())
    os.system('sudo date -s @"{:.0f}"'.format(timestamp))


# 得到系统时间
def getSysTime():
    current = datetime.now()
    return [current.second, current.minute, current.hour, current.day, current.month, current.year]


# 硬件时间录入系统时间
def hcToSys():
    date = readTime()
    date_str = f"20{date[5]:02}-{date[4]:02}-{date[3]:02} {date[2]:02}:{date[1]:02}:{date[0]:02}"
    setSysTime(date_str)


# 系统时间写入硬件时间
def sysToHc():
    date = getSysTime()
    writeTime(date)


if __name__ == "__main__":
    sysToHc()
