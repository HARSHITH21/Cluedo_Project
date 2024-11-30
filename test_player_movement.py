# test_player_movement.py

from player_movement import move_player

if __name__ == "__main__":
    # Set initial room
    current_room = 'Kitchen'

    # Test valid move
    current_room = move_player(current_room, 'Ballroom')
    print(f"Current room: {current_room}")

    # Test invalid move
    current_room = move_player(current_room, 'Library')
    print(f"Current room: {current_room}")
