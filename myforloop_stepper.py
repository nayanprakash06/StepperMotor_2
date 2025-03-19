# Write your code here :-)

from machine import Pin
from time import sleep

IN1 = Pin(12,Pin.OUT)
IN2 = Pin(13,Pin.OUT)
IN3 = Pin(14,Pin.OUT)
IN4 = Pin(15,Pin.OUT)

pins = [IN1,IN2,IN3,IN4]
steps = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
step_3 = [[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]
while True :
    for step in step_3 :
        for pin in range(len(pins)):
            pins[pin].value(step[pin])
            sleep(0.001)
