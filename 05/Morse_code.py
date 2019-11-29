import sys


def coding_function(dit, dah):
    code_funct = {
            "A":dit+dah+" ",
            "B":dah+dit*3+" ",
            "C":dah+dit+dah+dit+" ",
            "D":dah+dit*2+" ",
            "E":dit+" ",
            "F":dit*2+dah+dit+" ",
            "G":dah*2+dit+" ",
            "H":dit*4+" ",
            "I":dit*2+" ",
            "J":dit+dah*3+" ",
            "K":dah+dit+dah+" ",
            "L":dit+dah+dit*2+" ",
            "M":dah*2+" ",
            "N":dah+dit+" ",
            "O":dah*3+" ",
            "P":dit+dah*2+dit+" ",
            "Q":dah*2+dit+dah+" ",
            "R":dit+dah+dit+" ",
            "S":dit*3+" ",
            "T":dah+" ",
            "U":dit*2+dah+" ",
            "V":dit*3+dah+" ",
            "W":dit+dah*2+" ",
            "X":dah+dit*2+dah+" ",
            "Y":dah+dit+dah*2+" ",
            "Z":dah*2+dit*2+" ",
            " ":"/ "
            }
    return code_funct


def symbol_selection():
    print("Hi I'll convert your text into Morse code.")
    dit_dah = str(input("""If you wish to use different symbols (or group of symbols) than 
'.' for dit and '_' for dah write 'Pretty please' otherwise just press Enter:\n"""))
    if dit_dah == "Pretty please":
        dit = input("Specify dit (.): ")
        while dit == "":
            dit = input("I bet you don\'t want an empty symbol.\nSpecify dit (.): ")
        dah = input("Specify dah (_): ")
        while dah == "":
            dah = input("I bet you don\'t want an empty symbol.\nSpecify dah (_): ")
    else:
        dit = "."
        dah = "_"
    return dit, dah


def main():
    arguments = len(sys.argv)
    if arguments == 3:
        dit = sys.argv[1]
        dah = sys.argv[2]
    elif arguments > 3:
        return print("""If you want to specify more complicated symbols with spaces
please start again without arguments.""")
    else:
        dit, dah = symbol_selection()
    text = input("Now please insert the text you want to convert:\n")
    code_funct = coding_function(dit, dah)
    ciphered_text = ""
    for i in text.upper():
        ciphered_text += code_funct[i]
    return print(ciphered_text)


main()
