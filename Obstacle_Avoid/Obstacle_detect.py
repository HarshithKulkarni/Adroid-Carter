import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)

## Front Sensor ##

TRIG_front = 10
ECHO_front = 12

GPIO.setup(TRIG_front,GPIO.OUT)
GPIO.setup(ECHO_front,GPIO.IN)

## Back Sensor ##

TRIG_back = 26
ECHO_back = 24

GPIO.setup(TRIG_back,GPIO.OUT)
GPIO.setup(ECHO_back,GPIO.IN)

class Get_distance:

    def Front(self):

        GPIO.output(TRIG_front, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_front, False)

        while GPIO.input(ECHO_front) == False:
            start = time.time()
            
        while GPIO.input(ECHO_front) == True:
            end = time.time()

        sig_time = end-start
        distance = sig_time / 0.000058
        return distance

    def Back(self):

        GPIO.output(TRIG_back, True)
        time.sleep(0.00001)
        GPIO.output(TRIG_back, False)

        while GPIO.input(ECHO_back) == False:
            start = time.time()
            
        while GPIO.input(ECHO_back) == True:
            end = time.time()

        sig_time = end-start
        distance = sig_time / 0.000058
        return distance
    
