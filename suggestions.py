# suggestions.py

def make_suggestion(player_name, current_room, character, weapon):
    """
    Handles a player's suggestion.

    Args:
    - player_name: Name of the player making the suggestion.
    - current_room: The room the player is in (suggestions are valid only in this room).
    - character: Character suggested as the murderer.
    - weapon: Weapon suggested.

    Returns:
    - A formatted string describing the suggestion.
    """
    suggestion = (
        f"{player_name} suggests that {character} committed the crime "
        f"using the {weapon} in the {current_room}."
    )
    print(suggestion)
    return suggestion
