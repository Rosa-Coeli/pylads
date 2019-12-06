from random import randint, choice


def outer_squares(n):
    new_squares = input('''If you wish additional squares of random letters around your
text to further confuse anyone who might try to solve your cipher please tell me
how many otherwise type just press 'Enter':\n''')
    added_text = ''
    if new_squares == added_text:
        return n, added_text
    exponent = len(new_squares) - 1
    new_char = None
    for i in new_squares:
        print(i, int(i))
        if ((i != "0") and (i != "1") and (i != "2") and (i != "3") and (i != "4")
                and (i != "5") and (i != "6") and (i != "7") and (i != "8") and (i != "9")):
            print('Error: Invalid input.')
            n, added_text = outer_squares(n)
            break
        n += 2 * int(i) * 10**exponent
        exponent -= 1
        for j in range(4*(n-1)):
            new_char = random_char(new_char)
            added_text += new_char
    return n, added_text


def direction_f(starting_corner):
    while True:
        direction = input("""Set direction of the snake.\nFor clockwise type 'cw'.
For counter-clockwise type 'cc'.\n""")
        if direction == "cw":
            if starting_corner == '0':
                print(direction)
                return (0, 1), ((0, 1), (-1, 0))
            elif starting_corner == '1':
                return (-1, 0), ((0, 1), (-1, 0))
            elif starting_corner == '2':
                return (1, 0), ((0, 1), (-1, 0))
            elif starting_corner == '3':
                return (0, -1), ((0, 1), (-1, 0))
        elif direction == "cc":
            if starting_corner == '0':
                return (1, 0), ((0, -1), (1, 0))
            elif starting_corner == '1':
                return (0, 1), ((0, -1), (1, 0))
            elif starting_corner == '2':
                return (0, -1), ((0, -1), (1, 0))
            elif starting_corner == '3':
                return (-1, 0), ((0, -1), (1, 0))
        else:
            print('Error: Invalid input.\nTry again.')


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
            print('Error: Wrong input value.\nChose again.')


def starting_corner_position(starting_corner, n):
    if starting_corner == '0':
        return (0, 0)
    elif starting_corner == '1':
        return (n, 0)
    elif starting_corner == '2':
        return (0, n)
    elif starting_corner == '3':
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


def add_character(text, text_counter, ciphered_list, direction, n, position):
    ciphered_list[position[0]][position[1]] = text[text_counter]
    text_counter += 1
    return ciphered_list, text_counter


def direction_change(turn_matrix, direction, position):
    direction = (turn_matrix[0][0] * direction[0] + turn_matrix[0][1] * direction[1], 
                turn_matrix[1][0] * direction[0] + turn_matrix[1][1] * direction[1])
    position = position[0] + direction[0], position[1] + direction[1]
    return direction, position


def snake_line(text, text_counter, ciphered_list, direction, n, position):
    for i in range(n-1):
        ciphered_list, text_counter = add_character(text, text_counter, ciphered_list, direction, n, position)
        position = position[0] + direction[0], position[1] + direction[1]
    ciphered_list, text_counter = add_character(text, text_counter, ciphered_list, direction, n, position)
    return ciphered_list, text_counter, position


def snake_line_const(text, text_counter, ciphered_list, turn_matrix, direction, n, position):
    ciphered_list, text_counter, position = snake_line(text, text_counter, ciphered_list, direction, n, position)
    direction, position = direction_change(turn_matrix, direction, position)
    ciphered_list, text_counter = snake_line_sub(text, text_counter, ciphered_list, turn_matrix, direction, n, position)
    return ciphered_list, text_counter


def snake_line_sub(text, text_counter, ciphered_list, turn_matrix, direction, n, position):
    ciphered_list, text_counter, position = snake_line(text, text_counter, ciphered_list, direction, n, position)
    """for i in range(n-1):
        ciphered_list, text_counter = add_character(text, text_counter, ciphered_list, direction, n, position)
        position = position[0] + direction[0], position[1] + direction[1]
    ciphered_list, text_counter = add_character(text, text_counter, ciphered_list, direction, n, position)"""
    if n == 1:
        return ciphered_list, text_counter
    else:
        n -= 1
        direction, position = direction_change(turn_matrix, direction, position)
        """direction = (turn_matrix[0][0] * direction[0] + turn_matrix[0][1] * direction[1], 
                    turn_matrix[1][0] * direction[0] + turn_matrix[1][1] * direction[1])
        position = position[0] + direction[0], position[1] + direction[1]"""
        ciphered_list, text_counter = snake_line_const(text, text_counter, ciphered_list, turn_matrix, direction, n, position)
        return ciphered_list, text_counter


def main():
    starting_corner = starting_corner_set()
    print(starting_corner)
    direction, turn_matrix = direction_f(starting_corner)
    text = input('Insert the text you want to cipher:\n')
    text_modulo = len(text) % 4
    if  text_modulo != 0:
        text = rounded_text(text, 4-text_modulo)
    n = 2
    n, added_text = outer_squares(n)
    starting_corner = starting_corner_position(starting_corner, n-1)
    text = added_text + text
    ciphered_list = [["" for j in range(4)] for i in range(4)]
    text_counter = 0
    ciphered_list, text_counter = snake_line_sub(text, text_counter, ciphered_list, turn_matrix, direction, 4, starting_corner)
    #snake_line(turn_matrix, direction, n, position)
    for i in range(n):
        print(''.join(ciphered_list[i]))


main()
