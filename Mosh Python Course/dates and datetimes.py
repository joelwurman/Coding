from datetime import datetime, timedelta
from time import time

dt = datetime(2018, 12 , 1)
dt2 = datetime.now()
print(dt)
print('+')
print(dt2)
dt3 = datetime.strptime("2019//31/01", '%Y//%d/%m')
print(dt3.day)
print('duration')
duration = dt2 - dt3
print(duration.total_seconds())
