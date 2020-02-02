import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)  
GPIO.setwarnings(False)
class Drive:
    def __init__(self):
        ## Left Motors ##

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


        self.rpwm_left= GPIO.PWM(RPWM_left, 100)
        self.lpwm_left= GPIO.PWM(LPWM_left, 100)

        self.rpwm_left.start(0)

        self.lpwm_left.start(0)

        ## Right Motors ##

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


        self.rpwm_right= GPIO.PWM(RPWM_right, 100)
        self.lpwm_right= GPIO.PWM(LPWM_right, 100)

        self.rpwm_right.start(0)

        self.lpwm_right.start(0)

    def Forward(self):

        self.rpwm_right.ChangeDutyCycle(0) # Right Motor lpwm_right -> Forward, rpwm_right -> Backward
        self.rpwm_left.ChangeDutyCycle(0) # Left Motor lpwm_left -> Forward, rpwm_left -> Backward
        self.lpwm_right.ChangeDutyCycle(100) # Right Motor lpwm_right -> Forward, rpwm_right -> Backward
        self.lpwm_left.ChangeDutyCycle(100) # Left Motor lpwm_left -> Forward, rpwm_left -> Backward
        self.rpwm_right.ChangeDutyCycle(0) # Right Motor lpwm_right -> Forward, rpwm_right -> Backward
        self.rpwm_left.ChangeDutyCycle(0) # Left Motor lpwm_left -> Forward, rpwm_left -> Backward

        
    def Backward(self):
        
        self.lpwm_right.ChangeDutyCycle(0) # Right Motor lpwm_right -> Forward, rpwm_right -> Backward
        self.lpwm_left.ChangeDutyCycle(0) # Left Motor lpwm_left -> Forward, rpwm_left -> Backward
        self.rpwm_right.ChangeDutyCycle(100) # Right Motor lpwm_right -> Forward, rpwm_right -> Backward
        self.rpwm_left.ChangeDutyCycle(100) # Left Motor lpwm_left -> Forward, rpwm_left -> Backward
        self.lpwm_right.ChangeDutyCycle(0) # Right Motor lpwm_right -> Forward, rpwm_right -> Backward
        self.lpwm_left.ChangeDutyCycle(0) # Left Motor lpwm_left -> Forward, rpwm_left -> Backward
        
    def Stop(self):
        
        self.lpwm_right.ChangeDutyCycle(0) # Right Motor lpwm_right -> Forward, rpwm_right -> Backward
        self.lpwm_left.ChangeDutyCycle(0) # Left Motor lpwm_left -> Forward, rpwm_left -> Backward
        self.rpwm_right.ChangeDutyCycle(0) # Right Motor lpwm_right -> Forward, rpwm_right -> Backward
        self.rpwm_left.ChangeDutyCycle(0) # Left Motor lpwm_left -> Forward, rpwm_left -> Backward

    def Left(self):
        
        self.lpwm_left.ChangeDutyCycle(0)
        self.rpwm_right.ChangeDutyCycle(0)
        self.rpwm_left.ChangeDutyCycle(50)
        self.lpwm_right.ChangeDutyCycle(50)
        self.lpwm_left.ChangeDutyCycle(0)
        self.rpwm_right.ChangeDutyCycle(0)

    def Right(self):

        self.rpwm_left.ChangeDutyCycle(0)
        self.lpwm_right.ChangeDutyCycle(0)
        self.lpwm_left.ChangeDutyCycle(70)
        self.rpwm_right.ChangeDutyCycle(70)
        self.rpwm_left.ChangeDutyCycle(0)
        self.lpwm_right.ChangeDutyCycle(0)
