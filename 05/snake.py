from random import randint, choice


def direction_f(starting_corner):
    while True:
        direction = input("""Set direction of the snake.\nFor clockwise type 'cw'.
For counter-clockwise type 'cc'.\n""")
        if direction == "cw":
            if starting_corner == '0':
                print(direction)
                return (0, 1)
            elif starting_corner == '1':
                return (-1, 0)
            elif starting_corner == '2':
                return (0, -1)
            elif starting_corner == '3':
                return (1, 0)
        elif direction == "cc":
            if starting_corner == '0':
                return (1, 0)
            elif starting_corner == '1':
                return (0, 1)
            elif starting_corner == '2':
                return (-1, 0)
            elif starting_corner == '3':
                return (0, -1)
        else:
            print('Error: Invalid input.\nTry again:\n')


def starting_corner_set():
    while True:
        starting_corner = input("""Chose starting corner:
For upper left corner write 0.
For bottom left corner write 1.
For upper right corner write 2.
For bottom right corner write 3.\n""")
        if starting_corner == "0" or starting_corner == "1" or starting_corner == "2" or starting_corner == "3":
            return starting_corner
        else:
            print('Error: Wrong input value.\nChose again:\n')


def starting_corner_position(starting_corner, n):
    if starting_corner == 0:
        return (0, 0)
    elif starting_corner == 1:
        return (n, 0)
    elif starting_corner == 2:
        return (0, n)
    elif starting_corner == 3:
        return (n, n)


def random_char(last_char):
    if randint(0, 2) == 2:
        char_list = [chr(x) for x in range(ord("q"), ord("z")+1)]
    else:
        char_list = [chr(x) for x in range(ord("a"), ord("q"))]
    char = choice(char_list)
    return char if char != last_char else random_char(last_char)


def rounded_text(text, text_modulo):
    if text_modulo == 1:
        text += random_char(text[-1])
        return text
    else:
        text += random_char(text[-1])
        text = rounded_text(text, text_modulo-1)
        return text


def main():
    starting_corner = starting_corner_set()
    print(starting_corner)
    direction = direction_f(starting_corner)
    text = input('Insert the text you want to cipher:\n')
    text_modulo = len(text) % 4
    if  text_modulo != 0:
        text = rounded_text(text, 4-text_modulo)
    starting_corner = starting_corner_position(starting_corner, 4)

    print(text)


main()
