import sys


def seleiser():
    with open(sys.argv[1] + '.txt', 'a+', encoding='utf-8') as chapter:
        for word in sys.argv[2:]:
            i = 0
            while i < len(word):
                if word[i].lower() == 's':
                    if i < len(word)-1 and word[i+1] == 'e':
                        if i < len(word)-2 and word[i+2] == 'l':
                            if i == len(word)-3 or word[i+3] != 'e':
                                word = word[:i+3] + 'e' + word[i+3:]
                        else:
                            word = word[:i+2] + 'le' + word[i+2:]
                    elif i < len(word)-1 and word[i+1] == 'l':
                        if i < len(word)-2 and word[i+2] == 'e':
                            word = word[:i+1] + 'el' + word[i+2:]
                        else:
                            word = word[:i+1] + 'ele' + word[i+2:]
                    else:
                        word = word[:i+1] + 'ele' + word[i+1:]
                    i += 4
                elif word[i] == 'l':
                    if i < len(word)-1 and word[i+1] == 'e':
                        if i > 0 and word[i-1] == 'e':
                            word = word[:i-1] + 's' + word[i-1:]
                        elif i > 0 and word[i-1] == 'E':
                            word = 'Se' + word[i:]
                        else:
                            word = word[:i] + 'sel' + word[i+1:]
                    else:
                        word = word[:i] + 'sele' + word[i+1:]
                    i += 4
                elif word[i] == 'L':
                    if i < len(word)-1 and word[i+1] == 'e':
                        word = word[:i] + 'Sel' + word[i+1:]
                    else:
                        word = word[:i] + 'Sele' + word[i+1:]
                    i += 4
                else:
                    i += 1
            chapter.write(word + ' ')


seleiser()
