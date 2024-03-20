import os
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = []
    fileList = os.listdir("./data/杜良")
    fileList.sort()
    x = []
    y1 = []
    y2 = []
    select_x = []
    select_y1 = []
    select_y2 = []

    for dataTxtFile in fileList:
        with open(f"./data/杜良/{dataTxtFile}") as fp:
            data.extend(fp.readlines())
    # print(data)

    for line in data:
        if line[33] == ".":
            timeStamp = line[0: 19]
            sensor1 = line[28: 35]
            sensor2 = line[46: 53]
            cpuTmp = line[67: 71]
            gpuTmp = line[78: 82]
        else:
            timeStamp = line[0: 19]
            sensor1 = line[28: 36]
            sensor2 = line[47: 54]
            cpuTmp = line[68: 72]
            gpuTmp = line[79: 83]

        # print(timeStamp, " ", sensor1, " ", sensor2, " ", cpuTmp, " ", gpuTmp)
        x.append(timeStamp)
        y1.append(float(sensor1))
        y2.append(float(sensor2))
        if timeStamp[:10] == "2024-03-12":
            select_x.append(timeStamp)
            select_y1.append(float(sensor1))
            select_y2.append(float(sensor2))
            if float(sensor1) < 100 or float(sensor2) < 100:
                print(timeStamp, " ", sensor1, " ", sensor2)

    figure1 = plt.figure(1, figsize=(8, 3), dpi=1000)
    # plt.grid()
    plt.plot(x[::10], y1[::10], label="BH1715", linewidth=0.2)
    plt.plot(x[::10], y2[::10], label="BH1730", linewidth=0.2)
    plt.axvline(x="2024-03-12 00:00:02", color="r")
    plt.axvline(x="2024-03-13 00:00:02", color="r")
    plt.xlabel("time")
    plt.ylabel("Luminance/lux")
    plt.legend()
    plt.title("3-11 3-12 3-13  light sensor data")
    plt.figure(2, dpi=1000)
    plt.plot(select_x, select_y1, label="BH1715", linewidth=0.2)
    plt.plot(select_x, select_y2, label="BH1730", linewidth=0.2)
    plt.title("3-12 light sensor data")
    plt.show()
