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
- [License](#license)


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

Here’s a detailed **Installation Section** for your README file:

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


