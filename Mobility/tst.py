from Mobility import Drive as D
import time

obj = D()
while True:
    obj.Backward()
    time.sleep(1)
    obj.Left()
    time.sleep(1)
    obj.Stop()
