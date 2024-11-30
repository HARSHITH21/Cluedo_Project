# cluedo_game.py

from player_movement import move_player
from suggestions import make_suggestion
from solution_selector import select_solution

def cluedo_game():
    # Game setup
    print("Welcome to Cluedo!")
    solution = select_solution()  # Randomly select the murder mystery solution
    current_room = "Hall"  # Starting room for the player
    player_name = "Player 1"

    # Game instructions
    print("\nInstructions:")
    print("1. Move between rooms by typing the room name.")
    print("2. Make suggestions about the murderer, weapon, and room.")
    print("3. Your goal is to deduce the correct murderer, weapon, and room.")

    # Game loop
    while True:
        print(f"\nYou are currently in the {current_room}.")
        print("Rooms you can move to:", ", ".join(mansion_layout[current_room]))

        # Player move
        target_room = input("Enter the name of the room you want to move to (or 'quit' to exit): ").strip()
        if target_room.lower() == 'quit':
            print("Thanks for playing Cluedo! Goodbye.")
            break

        # Move the player
        current_room = move_player(current_room, target_room)

        # Allow suggestions
        if current_room != target_room:
            continue  # Skip if the move was invalid
        print("\nYou can now make a suggestion.")
        character = input("Who do you think the murderer is? ").strip()
        weapon = input("What weapon do you think was used? ").strip()

        # Make suggestion
        make_suggestion(player_name, current_room, character, weapon)

        # Check if the suggestion matches the solution
        if (character == solution['murderer'] and
                weapon == solution['weapon'] and
                current_room == solution['room']):
            print("\n🎉 Congratulations! You solved the murder mystery!")
            print("The correct solution was:")
            print(f"Murderer: {solution['murderer']}")
            print(f"Weapon: {solution['weapon']}")
            print(f"Room: {solution['room']}")
            break
        else:
            print("\nYour suggestion was incorrect. Keep playing!")

if __name__ == "__main__":
    from mansion_layout import mansion_layout
    cluedo_game()
