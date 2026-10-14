from machine import Pin, PWM
import time
import random

red = Pin(16, Pin.OUT)
yellow = Pin(17, Pin.OUT)
green = Pin(18, Pin.OUT)

red_button = Pin(13, Pin.IN, Pin.PULL_DOWN)
yellow_button = Pin(14, Pin.IN, Pin.PULL_DOWN)
green_button = Pin(15, Pin.IN, Pin.PULL_DOWN)

start_button = Pin(0, Pin.IN, Pin.PULL_DOWN)

buzzer = PWM(Pin(1 ))

colors = [red, yellow, green]
sequence = []
game = True

countdown = [3, 2, 1]

# Buzzer function
def beep(color, duration):   
    if color == red:
        frequency = 300

    elif color == yellow:
        frequency = 500

    elif color == green:
        frequency = 700
        
    buzzer.freq(frequency)
    buzzer.duty_u16(32768)
    time.sleep(duration)
    buzzer.duty_u16(0)

# Game over sound
def game_over_sound():
    buzzer.freq(1000)
    buzzer.duty_u16(32768)
    time.sleep(2)
    buzzer.duty_u16(0)
    
# Wait for Start button
# 'while' runs a continuous loop of 0.01sec waiting for button value to become 1
while start_button.value() == 0:
    time.sleep(0.01)

for i in countdown:
    print(i)
    buzzer.freq(100)
    buzzer.duty_u16(32768)
    time.sleep(0.5)
    buzzer.duty_u16(0)
    time.sleep(1)

print("GO!")

while game:
    
    #Generate random number
    chosen = random.choice(colors)
    sequence.append(chosen)
    
    for color in sequence:
        color.value(1)
        beep(color, 0.5)
        time.sleep(1)
        color.value(0)
        time.sleep(0.5)
        

    for color in sequence:    
    # Wait for user clicks buttons
        print("Waiting for player input...")
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
            game_over_sound()
            game = False
            break
        
        while (red_button.value() == 1 or
                   yellow_button.value() == 1 or
                   green_button.value() == 1):
            time.sleep(0.01)
    
    
    
    
    
