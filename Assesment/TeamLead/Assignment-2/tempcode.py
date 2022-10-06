#from machine import Pin
import random
from time import sleep
#btn=Pin(4,Pin.IN)
while True:
 temp = random.randint(1,100)
 print("current temp=",temp)
 humid = random.randint(1,100)
 print("current humid=",humid)
 if(temp>=50 and humid<35):
  print("Alarm On")
 else:
  print("Alarm Off")
  sleep(2) 
