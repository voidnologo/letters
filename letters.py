# -- coding: utf-8 --


import random
import subprocess
import sys
import time

import assets
from color import Colorize
from read_char import ReadChar


VOICES = assets.get_system_voices()


def get_input(prompt):
    with ReadChar() as rc:
        char = rc.upper()
        if char in ['\x03']:
            sys.exit()
        return char


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
    return random.choice(VOICES)


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


def interact(letter):
    execute_shell_command('clear')
    display_letter(letter)
    say_letter(letter)


def main():
    print(get_phrase('exit'))
    time.sleep(3)
    while True:
        letter = get_letter()
        correct = False
        while not correct:
            interact(letter)
            guess = get_input(prompt())
            correct = check_input(guess, letter)


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        pass
