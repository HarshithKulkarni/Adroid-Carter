import RPi.GPIO as GPIO
import time

GPIO.setwarnings(False)
# doing this first, since we're using a while True.
GPIO.cleanup()

GPIO.setmode(GPIO.BOARD)
TRIG = 26
ECHO = 24

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)


def get_distance():


    GPIO.output(TRIG, True)
    time.sleep(0.00001)
    GPIO.output(TRIG, False)

    while GPIO.input(ECHO) == False:
        start = time.time()

    while GPIO.input(ECHO) == True:
        end = time.time()

    sig_time = end-start

    #CM:
    distance = sig_time / 0.000058

    #inches:
    #distance = sig_time / 0.000148
    print('Distance: {} centimeters'.format(distance))

    return distance


while True:
    distance = get_distance()
    time.sleep(1)
