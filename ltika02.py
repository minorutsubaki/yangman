#     ltika page 102  2022 09 24 sainyuuryoku
#     kadoukakuninnzumi 
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT)

print('ctr-c  de syuuryou')
try:
    while True:
        sleep (0.01)
        GPIO.output(25, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(25, GPIO.LOW)
        sleep (0.5)
        
except KeyboardInterrupt:
    pass
GPIO.cleanup()
print('GPIO.cleanup !')

