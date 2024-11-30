# test_suggestions.py

from suggestions import make_suggestion

if __name__ == "__main__":
    # Test a valid suggestion
    suggestion = make_suggestion(
        player_name="Player 1",
        current_room="Library",
        character="Miss Scarlett",
        weapon="Candlestick"
    )

    # Print the suggestion (already printed in the function)
    print("\nReturned Suggestion String:")
    print(suggestion)
