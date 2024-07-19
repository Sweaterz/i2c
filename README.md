# README
Python脚本用以控制BH1715以及BH1730传感器.  
crontab每分钟启动一次进行10次光线监测.  😄  


**lightSensor.py**  
调用BH1715和BH1730两个传感器.

## 2024-03-27 Wed. 09:12 
**RTC_RX8025T.py**
调用RTC_RX8025T时钟功能，完成芯片写入系统时间或者系统时间写入芯片.

针对您的需求，请要使用请在main函数中调用:
```python 
# 1.读取时钟芯片的时间
def readTime()

# 2.写入时间到RX8025
def writeTime()

# 3.系统时间写入硬件时间
def sysToHc()

# 4.硬件时间录入系统时间
def hcToSys()
```
本程序仅供参考，请根据您的需求进行修改.
考虑到由于功能比较简单，本程序没有使用类的编写方式，您可以根据您的需求便于进行修改.