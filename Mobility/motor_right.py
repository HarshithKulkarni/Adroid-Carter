import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)


RPWM_right = 23
LPWM_right = 24

L_EN_right = 6
R_EN_right = 13


GPIO.setup(RPWM_right, GPIO.OUT)
GPIO.setup(LPWM_right, GPIO.OUT)
GPIO.setup(L_EN_right, GPIO.OUT)
GPIO.setup(R_EN_right, GPIO.OUT)

GPIO.output(R_EN_right, True)
GPIO.output(L_EN_right, True)


rpwm_right= GPIO.PWM(RPWM_right, 100)
lpwm_right= GPIO.PWM(LPWM_right, 100)

rpwm_right.start(0)

lpwm_right.start(0)

while 1:
      lpwm_right.ChangeDutyCycle(100)
      
