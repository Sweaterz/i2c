import os
import matplotlib.pyplot as plt


def read_data(path):
    """Read data from path"""
    data = []
    fileList = os.listdir(path)
    for dataTxtFile in fileList:
        with open(f"{path}/{dataTxtFile}") as fp:
            data.extend(fp.readlines())
    return data


def parse_data(data):
    """Parse data into x, y1, y2"""
    x = []
    y1 = []
    y2 = []
    for line in data:
        timeStamp = line[0: 19]
        sensor1 = line[34: 42]
        sensor2 = line[54: 62]
        x.append(timeStamp)
        try:
            y1.append(float(sensor1))
            y2.append(float(sensor2))
        except ValueError:
            pass # Handle any exception here if needed
    return x, y1, y2


def plot_data(x, y1, y2):
    """Plot data"""
    plt.figure(figsize=(20, 10), dpi=200)
    plt.grid()
    plt.bar(x[::10], y1[::10], label="BH1715")
    plt.bar(x[::10], y2[::10], label="BH1730")
    plt.xlabel("time")
    plt.ylabel("Luminance/lux")
    plt.xticks(rotation='vertical')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    data = read_data("./data")
    x, y1, y2 = parse_data(data)
    plot_data(x, y1, y2)
