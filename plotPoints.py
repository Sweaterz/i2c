import os
import matplotlib.pyplot as plt

if __name__ == "__main__":
    data = []
    fileList = os.listdir("./data")
    x = []
    y1 = []
    y2 = []
    for dataTxtFile in fileList:
        with open(f"./data/{dataTxtFile}") as fp:
            data.extend(fp.readlines())
    print(data)

    for line in data:
        timeStamp = line[0: 19]
        sensor1 = line[34: 42]
        sensor2 = line[54: 62]
        print(timeStamp," ", sensor1, " ",sensor2)
        x.append(timeStamp)
        y1.append(float(sensor1))
        y2.append(float(sensor2))


    plt.figure(figsize=(8, 3), dpi=1000)
    plt.grid()
    plt.plot(x[::10], y1[::10], label="BH1715")
    plt.plot(x[::10], y2[::10], label="BH1730")
    plt.xlabel("time")
    plt.ylabel("Luminance/lux")
    plt.legend()
    plt.show()
