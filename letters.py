import random
import subprocess
import time

import assets
from color import Colorize


def get_input(prompt):
    return input(prompt).upper()


def check_input(guess, letter):
    pressed_phrase = get_phrase('pressed').format(guess)
    voice = get_random_voice()
    say_phrase(pressed_phrase, voice)
    if guess == letter:
        color = 'FG_BOLD_GREEN'
        text = '\n{}\n'.format(assets.OK)
        print(Colorize.colorize(color, text))
        say_phrase(get_phrase('correct'), voice)
        return True
    else:
        color = 'FG_BOLD_RED'
        text = '\n{}\n'.format(assets.X)
        print(Colorize.colorize(color, text))
        say_phrase(get_phrase('wrong'), voice)
        return False


def get_random_color():
    return random.choice(list(Colorize.colors.keys()))


def get_letter():
    return random.choice(list(assets.BLOCKS.keys()))


def get_phrase(key):
    return random.choice(assets.PHRASES[key])


def get_random_voice():
    return random.choice(assets.VOICES)


def say_phrase(sentence, voice):
    cmd = "say -v '{}' '{}'".format(voice, sentence)
    execute_shell_command(cmd)


def say_letter(letter):
    kind = number_or_letter(letter)
    phrase = get_phrase('letter').format(kind, letter)
    voice = get_random_voice()
    say_phrase(phrase, voice)


def execute_shell_command(cmd):
    subprocess.call(cmd, shell=True)


def number_or_letter(char):
    return 'letter' if char.isalpha() else 'number'


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
        say_letter(letter)
        correct = False
        while not correct:
            guess = get_input(prompt())
            correct = check_input(guess, letter)
        time.sleep(3)
        execute_shell_command('clear')


if __name__ == '__main__':
    main()
