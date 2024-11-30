# characters.py

# Define the characters and their starting positions
characters = {
    'Miss Scarlett': 'Hall',
    'Colonel Mustard': 'Lounge',
    'Mrs. White': 'Kitchen',
    'Mr. Green': 'Conservatory',
    'Mrs. Peacock': 'Library',
    'Professor Plum': 'Study'
}

# Function to display characters and their positions
def display_characters():
    print("Characters and their starting positions:")
    for character, position in characters.items():
        print(f"{character}: starts in {position}")
