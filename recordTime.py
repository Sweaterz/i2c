from RTC_RX8025T import readTime, getSysTime

if __name__ == '__main__':
    registerTime = readTime()
    systemTime = getSysTime()
    print(registerTime)
    print(systemTime)
    content = ""
    with open("~/recordTime/record.txt") as fp:
        fp.write(content)
