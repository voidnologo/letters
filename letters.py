import random
import subprocess
import time

import assets
from color import Colorize


def get_input(prompt):
    return input(prompt).upper()


def check_input(guess, letter):
    if guess == letter:
        color = 'FG_BOLD_GREEN'
        text = '\n{}\n'.format(assets.OK)
        print(Colorize.colorize(color, text))
        return True
    else:
        color = 'FG_BOLD_RED'
        text = '\n{}\n'.format(assets.X)
        print(Colorize.colorize(color, text))
        return False


def get_random_color():
    return random.choice(list(Colorize.colors.keys()))


def get_letter():
    return random.choice(list(assets.BLOCKS.keys()))


def display_letter(letter):
    color = get_random_color()
    text = '\n{}\n'.format(assets.BLOCKS[letter])
    print(Colorize.colorize(color, text))


def prompt():
    return '\nEnter the character :>>> '


def main():
    while True:
        letter = get_letter()
        display_letter(letter)
        correct = False
        while not correct:
            guess = get_input(prompt())
            correct = check_input(guess, letter)
        time.sleep(3)
        subprocess.call('clear', shell=True)


if __name__ == '__main__':
    main()
