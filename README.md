# 🎮 Pico Simon Says — Interactive Memory Game

An interactive, hardware-based **Simon Says memory game** developed using the **Raspberry Pi Pico and MicroPython**.

The game challenges players to memorize and repeat increasingly complex LED sequences using physical push buttons. A 16×2 I2C LCD provides real-time feedback, displaying instructions, game progress, and scores.

This project explores embedded systems programming, GPIO communication, hardware integration, and interactive game development.

## 🎯 Project Objectives

- Develop an interactive memory game using the Raspberry Pi Pico.
- Interface physical input and output components using MicroPython.
- Implement randomized sequences and player input validation.
- Design a progressive difficulty system.
- Display real-time game information through an I2C LCD.
- Explore modular programming and embedded software development.

## 🛠️ Hardware Components

| Component | Purpose |
|---|---|
| Raspberry Pi Pico | Main microcontroller |
| 16×2 I2C LCD | Displays game status, levels, and scores |
| 4 LEDs | Display randomized sequences |
| 4 Push Buttons | Allow players to repeat sequences |
| 220–330Ω Resistors | Limit current through LEDs |
| Breadboard | Circuit assembly |
| Jumper Wires | Hardware connections |
| Potentiometer (Optional) | Adjustable difficulty settings |

## 🧠 How It Works

**1. Game Initialization**

The LCD displays a welcome screen and prompts the player to begin.

**2. Sequence Generation**

The Pico randomly selects an LED and flashes it.

**3. Player Input**

The player presses the button corresponding to the illuminated LED.

**4. Sequence Validation**

The program compares the player's input against the generated sequence.

- Correct sequence → Advance to the next level.
- Incorrect sequence → Game over.

**5. Progressive Difficulty**

Each successful round adds another LED to the sequence, increasing the memory challenge.

**6. Game Over**

The LCD displays the player's final score and provides an option to restart.

### Example Gameplay

**Level 1:**
🔴

**Level 2:**
🔴 → 🟢

**Level 3:**
🔴 → 🟢 → 🔵

**Level 4:**
🔴 → 🟢 → 🔵 → 🟡

The sequence continues growing until the player makes a mistake.

