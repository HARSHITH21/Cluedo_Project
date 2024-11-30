# Cluedo Game
## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [File Descriptions](#file-descriptions)
- [Example Gameplay](#example-gameplay)
- [Future Enhancements](#future-enhancements)
- [Authors](#authors)



## Overview
This project is a digital implementation of the classic murder mystery board game **Cluedo (Clue)**. Players move between rooms, make suggestions, and solve the murder mystery using deduction and logic. The game is implemented in Python and provides an interactive command-line experience.

---

## Features
- **Mansion Layout**: A connected graph of rooms, representing the mansion where the crime occurred.
- **Characters**: Six unique suspects with predefined starting positions.
- **Weapons**: Six classic murder weapons.
- **Player Movement**: Navigate between rooms based on valid connections.
- **Suggestions**: Players can make suggestions about the murderer, weapon, and room when entering a room.
- **Random Solution Generator**: A randomly selected murderer, weapon, and room serve as the solution to the mystery.
- **Interactive Gameplay**: A dynamic command-line interface where players make decisions and deductions.

---

## Prerequisites
- Python 3.7 or higher

---

## **Installation**

Follow these steps to set up and run the Cluedo game:

#### **1. Clone the Repository**
Download the project from GitHub by cloning the repository:
```bash
git clone https://github.com/HARSHITH21/Cluedo_Project.git
cd Cluedo_Project
```

#### **2. Ensure Python is Installed**
Make sure Python 3.7 or higher is installed on your system:
- To check the Python version:
  ```bash
  python --version
  ```
  Or, if using `python3`:
  ```bash
  python3 --version
  ```

#### **3. Install Dependencies**
If any external libraries are required, install them using `pip`. (Currently, the project does not require any external dependencies, but you can create a `requirements.txt` file for future use.)

To install dependencies from a `requirements.txt` file:
```bash
pip install -r requirements.txt
```

#### **4. Run the Game**
Start the game by running the main script:
```bash
python cluedo_game.py
```
Or, if using `python3`:
```bash
python3 cluedo_game.py
```

#### **5. Gameplay**
Follow the instructions displayed in the terminal to navigate rooms, make suggestions, and solve the mystery.

This looks fantastic! You've got a clean and organized README file with clear instructions under the **Installation** section.

If you want to complete the rest of the README, here's how the remaining sections can look:

---

## **How to Play**
1. **Start the Game**:
   - The game begins with the player in the "Hall."

2. **Move Between Rooms**:
   - Enter the name of a connected room to move.
   - You can only move to rooms directly connected to your current location.

3. **Make Suggestions**:
   - After entering a room, suggest:
     - **Who** committed the crime (a character).
     - **What** weapon was used.
     - **Where** the crime occurred (the current room).

4. **Win the Game**:
   - If your suggestion matches the randomly generated solution, you win!
   - Otherwise, continue making moves and suggestions until you solve the mystery.

---

## **File Descriptions**
- **`mansion_layout.py`**: Defines the layout of the mansion, including room connections.
- **`characters.py`**: Contains definitions of the characters and their starting positions.
- **`weapons.py`**: Lists all weapons available in the game.
- **`player_movement.py`**: Implements the logic for player movement between rooms.
- **`suggestions.py`**: Handles the logic for making suggestions during gameplay.
- **`solution_selector.py`**: Randomly generates the solution to the murder mystery.
- **`cluedo_game.py`**: The main script that integrates all components and manages the gameplay loop.
- **Test Files**:
  - **`test_mansion_layout.py`**: Tests for mansion layout functionality.
  - **`test_characters_and_weapons.py`**: Tests for characters and weapons.
  - **`test_player_movement.py`**: Tests for player movement logic.
  - **`test_suggestions.py`**: Tests for suggestion logic.

---

## **Example Gameplay**
Below is an example of what gameplay might look like:

```text
Welcome to Cluedo!

Instructions:
1. Move between rooms by typing the room name.
2. Make suggestions about the murderer, weapon, and room.
3. Your goal is to deduce the correct murderer, weapon, and room.

You are currently in the Hall.
Rooms you can move to: Lounge, Study
Enter the name of the room you want to move to (or 'quit' to exit): Lounge
Player moved from Hall to Lounge.

You can now make a suggestion.
Who do you think the murderer is? Miss Scarlett
What weapon do you think was used? Rope
Player 1 suggests that Miss Scarlett committed the crime using the Rope in the Lounge.

Your suggestion was incorrect. Keep playing!
```

---

## **Future Enhancements**
Here are some ideas for improving the game in the future:
- Add support for multiple players.
- Introduce AI opponents to make their own suggestions.
- Enhance the interface for a more user-friendly experience.
- Include a graphical user interface (GUI) for broader accessibility.

---

## **Authors**
- [Your Name]

---
