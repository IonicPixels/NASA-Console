import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)


GPIO.output(18,GPIO.HIGH)
time.sleep(30)
GPIO.output(18,GPIO.LOW)

