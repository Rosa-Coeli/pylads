import sys


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
        print("""If you want to specify more complicated symbols with spaces
please start again without arguments.""")
    else:
        dit, dah = symbol_selection()


main()
