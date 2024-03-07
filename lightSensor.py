import os
import time

import BH1715
import BH1730

def read_sensor_data(sensor, default_value=0):
    try:
        return sensor.detect()
    except Exception as e:
        print(f"Error reading from {sensor.__name__}: {e}")
        return default_value

if __name__ == '__main__':
    # 可配置部分
    log_format = ".txt"
    file_name = f"{time.strftime('%Y-%m-%d', time.localtime())}{log_format}"
    sleep_interval = 1  # 数据采集间隔时间
    round = 10 # 采集次数
    temp_cpu = None
    temp_gpu = None
    if not os.path.exists("/home/hk/workspace/save"):
        os.sys.exit(1)
    with open(file_name, 'a') as file:
        for i in range(round):
            lumi15 = read_sensor_data(BH1715, default_value=-1)
            lumi30 = read_sensor_data(BH1730, default_value=-1)
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            if lumi15 == -1 or lumi30 == -1:
                content = formatted_time + " ERROR: Fail to get light sensor data. "
            else:
                content = formatted_time + " BH1715: {:.2f}lux    BH1730: {:.2f}lux".format(lumi15, lumi30)
            
            with open("/sys/devices/virtual/thermal/thermal_zone0/temp") as temp_fp1:
                temp_cpu = int(temp_fp1.read()) / 1000
            with open("/sys/devices/virtual/thermal/thermal_zone2/temp") as temp_fp2:
                temp_gpu = int(temp_fp2.read()) / 1000
            content += "temp CPU: {:.2f}°C GPU:{:.2f}°C \n".format(temp_cpu, temp_gpu)
            print(content, end="")
            file.write(content)
            time.sleep(sleep_interval)
