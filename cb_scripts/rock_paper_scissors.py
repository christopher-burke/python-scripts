#!/usr/bin/env python3

"""Rock, Paper, scissors."""


from random import choice


def computer():
    """Return the computer player"s choice."""
    return choice(["ROCK", "PAPER", "SCISSORS"])


def player():
    """Get the player"s choice."""
    input_ = ""
    if input_ not in ["ROCK", "PAPER", "SCISSORS"]:
        input_ = str(input("ROCK, PAPER, SCISSORS? ")).upper()
    return input_


def game(computer_input: str, player_input: str):
    """Logic for game, returns the winner."""
    computer = computer_input
    player = player_input
    results = (computer, player)

    print(f"Computer choose {computer}. You choose {player}.")

    if computer == player:
        return "TIE"
    if results in [("ROCK", "PAPER"),
                   ("PAPER", "SCISSORS"),
                   ("SCISSORS", "ROCK"), ]:
        return f"You win!"
    else:
        return "Computer wins."


def main():
    """Run the game."""
    while True:
        result = game(computer_input=computer(),
                      player_input=player())
        print(f"{result}")
        if result != "TIE":
            break

    return result


if __name__ == "__main__":
    main()
