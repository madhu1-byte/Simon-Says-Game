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

start_button = Pin(xx, Pin.IN, Pin.PULL_DOWN)

countdown = [3, 2, 1]

# Wait for Start button
# 'while' runs a continuous loop of 0.01sec waiting for button value to become 1
while start_button.value() == 0:
    time.sleep(0.01)

for i in countdown:
    print(i)
    time.sleep(1)

print("GO!")

while game:
    
    #Generate random number
    chosen = random.choice(colors)
    sequence.append(chosen)
    
    for color in sequence:
        color.value(1)
        time.sleep(1)
        color.value(0)
        time.sleep(0.5)
        

    for color in sequence:    
    # Wait for user clicks buttons
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
    
        if player_color != color:
            print("GAME OVER")
            game = False
            break
        
        while (red_button.value() == 1 or
                   yellow_button.value() == 1 or
                   green_button.value() == 1):
            time.sleep(0.01)
    
    
    
    
    
