import sys
from snake_functions import random_char


def main():
    text = input('Please type your text:\n') if len(sys.argv) == 1 else ''.join(sys.argv[1:])
    ciphered_text = ''
    for letter in text:
        if letter.isalnum():
            ciphered_text += (letter+random_char(letter)).upper()
    print(ciphered_text)


main()
