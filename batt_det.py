import psutil
import time
def bat_details():
        while True:
            b = psutil.sensors_battery()
            p = b.percent
            return p

# while True:
#     time.sleep(10)
#     print(bat_details())