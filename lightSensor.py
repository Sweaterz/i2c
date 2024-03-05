import os
import time

import BH1715
import BH1730


if __name__ == '__main__':

    current_date = time.strftime("%Y-%m-%d", time.localtime())
    log_format = ".txt"
    file_name = current_date + log_format
    with open(file_name, 'a') as file:
        for i in range(10):
            lumi15 = BH1715.detect()
            lumi30 = BH1730.detect()
            formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            content = formatted_time + "    BH1715:" + str(lumi15) + "lux    BH1730:" + str(lumi30) + "lux\n"
            file.write(content)
            time.sleep(1)
