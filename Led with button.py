import RPi.GPIO as GPIO
from gpiozero import LED
from gpiozero import Button
from time import sleep
led = LED(17)
button = Button(3)
l = 0
while True :
    if button.is_pressed:
        if l == 1:
            l = 0
            sleep(0.5)
            print(l)
        elif l == 0 :
            l = 1
            sleep(0.5)
            print(l)
    if l == 1:
        led.on()
    if l == 0:
        led.off()