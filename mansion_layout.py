# mansion_layout.py

# Define the mansion layout as a graph
mansion_layout = {
    'Kitchen': ['Ballroom', 'Dining Room'],
    'Ballroom': ['Kitchen', 'Conservatory'],
    'Dining Room': ['Kitchen', 'Lounge'],
    'Conservatory': ['Ballroom', 'Library'],
    'Lounge': ['Dining Room', 'Hall'],
    'Library': ['Conservatory', 'Study'],
    'Hall': ['Lounge', 'Study'],
    'Study': ['Library', 'Hall']
}

# Function to display the layout
def display_mansion_layout():
    print("Mansion Layout:")
    for room, connections in mansion_layout.items():
        print(f"{room}: connected to {', '.join(connections)}")
