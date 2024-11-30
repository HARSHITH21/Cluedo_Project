# player_movement.py

from mansion_layout import mansion_layout

# Function to move a player between rooms
def move_player(current_room, target_room):
    if target_room in mansion_layout[current_room]:
        print(f"Player moved from {current_room} to {target_room}.")
        return target_room
    else:
        print(f"Cannot move from {current_room} to {target_room}. Invalid move.")
        return current_room
