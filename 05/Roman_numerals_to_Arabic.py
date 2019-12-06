import sys

def main():
    roman_num = sys.argv[1]
    function_dict = {'I':1,
                     'V':5,
                     'X':10,
                     'L':50,
                     'C':100,
                     'D':500,
                     'M':1000}
    sum_value = 0
    current_digit = function_dict[roman_num[0]]
    for i in range(1, len(roman_num)):
        next_digit = function_dict[roman_num[i]]
        sum_value += current_digit if current_digit >= next_digit else -current_digit
        current_digit = next_digit
    sum_value += current_digit
    print(sum_value)


main()
