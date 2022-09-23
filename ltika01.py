#   ltika 01 toguruswit  pip RPi.GPIO  2023 09 22 3rd inputed




import RPi.GPIO as GPIO
from time import sleep

def my_callback(channel):
    global ledState
    if channel == 27:
        ledState = not ledState
        if ledState == GPIO.HIGH:
            GPIO.output(25, GPIO.HIGH)
            
        else:
            GPIO.output(25, GPIO.LOW)
            
GPIO.setmode(GPIO.BCM)
GPIO.setup(25, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.add_event_detect(27, GPIO.RISING, callback = my_callback, bouncetime=200)

ledState = GPIO.LOW

try:
    while True:
        sleep (0.01)
        
except KeyboardInterrupt:
    pass
GPIO.cleanup()

