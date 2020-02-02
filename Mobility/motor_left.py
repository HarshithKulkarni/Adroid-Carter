import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)


RPWM_left = 19;
LPWM_left = 26;

L_EN_left = 20;
R_EN_left = 21;


GPIO.setup(RPWM_left, GPIO.OUT)
GPIO.setup(LPWM_left, GPIO.OUT)
GPIO.setup(L_EN_left, GPIO.OUT)
GPIO.setup(R_EN_left, GPIO.OUT)

GPIO.output(R_EN_left, True)
GPIO.output(L_EN_left, True)


rpwm_left= GPIO.PWM(RPWM_left, 100)
lpwm_left= GPIO.PWM(LPWM_left, 100)

rpwm_left.start(0)

lpwm_left.start(0)
while 1:
      lpwm_left.ChangeDutyCycle(100)
      
