from random import randint, choice


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
    start_corner = input("""Chose starting corner:
    -For upper left corner write 0.
    -For bottom left corner write 1.
    -For upper right corner write 2.
    -For bottom right corner write 3.""")
    text = input('Insert the text you want to cipher:\n')
    text_modulo = len(text) % 4
    if  text_modulo != 0:
        text = rounded_text(text, 4-text_modulo)

    print(text)


main()
