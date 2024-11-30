# solution_selector.py

import random
from characters import characters
from weapons import weapons
from mansion_layout import mansion_layout

# Randomly select the solution to the murder mystery
def select_solution():
    murderer = random.choice(list(characters.keys()))
    weapon = random.choice(weapons)
    room = random.choice(list(mansion_layout.keys()))
    return {'murderer': murderer, 'weapon': weapon, 'room': room}

# Function to display the solution (for testing purposes)
def display_solution(solution):
    print("The murder mystery solution is:")
    print(f"Murderer: {solution['murderer']}")
    print(f"Weapon: {solution['weapon']}")
    print(f"Room: {solution['room']}")
