def change_computing(change):
    function = {}
    for i in 'A' 'a':
        order = ord(i)
        for j in range(order, order+26):
            function[chr(j)] = chr((j - order + change) % 26 + order)
    return function


def ciphering(text, function):
    pass


def main():
    print("Hi, I will cipher your text with Caesar cipher")
    text = input("Insert text you want to cipher: ")
    change = int(input("Specify number: "))
    function = change_computing(change)
    #return ciphering(text, function)
    print(function)


main()
