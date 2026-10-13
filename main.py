from machine import Pin
import time
import random

red = Pin(xx, Pin.OUT)
yellow = Pin(xx, Pin.OUT)
green = Pin(xx, Pin.OUT)

red_button = Pin(xx, Pin.IN, Pin.PULL_DOWN)
yellow_button = Pin(xx, Pin.IN, Pin.PULL_DOWN)
green_button = Pin(xx, Pin.IN, Pin.PULL_DOWN) 

colors = [red, yellow, green]
sequence = []
game = True

# set up pin 15 as an input with a pull-down resistor
start_button = Pin(xx, Pin.IN, Pin.PULL_DOWN)

countdown = [3, 2, 1]
if start_button.value() == 1:
    for i in countdown:
        print (i)
        time.sleep(1)
    print("GO!")

while start_button.value() == 1:
    
    chosen = random.choice(colors)
    sequence.append(chosen)
    
    for color in sequence:
        color.value(1)
        time.sleep(1)
        color.value(0)
        time.sleep(0.5)
        

    
# Now user clicks buttons
while (red_button.value() == 0 and
       yellow_button.value() == 0 and
       green_button.value() == 0):
    time.sleep(0.01)
    
# translating button color to led color    
if red_button.value() == 1:
    player_color = red

elif yellow_button.value() == 1:
    player_color = yellow

elif green_button.value() == 1:
    player_color = green
    
    
    
    
    
