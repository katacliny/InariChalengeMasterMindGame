from enum import Enum
import random
from os import system, name
from colorama import Fore, init
import colorama
from texts import *


init()
exit_game = False
show_intro = True
last_message = ""
all_inputs = []


class Colors(Enum):
    R = 1  # Red
    B = 2  # Blue
    Y = 3  # Yellow
    G = 4  # Green
    W = 5  # White
    O = 6  # Orange


secret = random.sample(list(Colors.__members__.keys()), 4)


def get_pegs(sequence: str, secret):

    white_pegs = 0
    black_pegs = 0

    for idx, val in enumerate(list(sequence)):

        if val == secret[idx]:

            black_pegs += 1

        elif val in secret:

            white_pegs += 1

        else:
            pass

    if black_pegs == len(sequence):
        global exit_game
        exit_game = True
        return "You win !"

    else:
        return f"Black pegs: {black_pegs}, White pegs: {white_pegs} (?) Black pegs means 'Black pegs tell you how many pegs of your guess you have correct in color and position'. White pegs means 'white pegs tell you how many pegs of ur guess you have correct in color but not in the proper position'."


def validate_color_sequence(sequence: str):

    if not len(sequence) == 4:
        return False

    if not set(list(sequence)).issubset(list(Colors.__members__.keys())):
        return False

    return True


def validate_help(sequence: str):

    if not sequence == "--help":
        return False

    return True


def validate_command(sequence: str):

    if sequence == "--exit":
        global exit_game
        exit_game = True
        return exit_game

    return False


def game():
    system("clear")
    title()
    global show_intro
    if show_intro:
        show_intro = False
        intro()

    global last_message
    print(Fore.RED)
    print(last_message)
    print(f"All Attempts {all_inputs}")
    print("--------------------------------------------------------------------------")
    print(Fore.CYAN)
    print(
        f"The list of possible colors is {str(list(Colors.__members__.keys()))} you only can use a 4 colors combination."
    )
    sequence: str = input(
        "Insert a color sequence or type --help to see a lit of all possible options: "
    )
    print(Fore.RED)
    print("--------------------------------------------------------------------------")
    all_inputs.append(sequence)
    if validate_color_sequence(sequence):
        last_message = get_pegs(sequence, secret)

    elif validate_help(sequence):
        help_log(Colors)

    elif validate_command(sequence):
        print("Done!")

    else:
        print("Wrong input please use --help to get all possible options.")

    if not exit_game:
        game()



if __name__ == "__main__":
    game()
