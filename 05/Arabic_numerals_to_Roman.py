import sys


def conversion(l, m, h, digit):
    function_hash = {'0':'',
                     '1':l,
		     '2':2*l,
		     '3':3*l,
		     '4':l+m,
		     '5':m,
		     '6':m+l,
		     '7':m+2*l,
		     '8':m+3*l,
		     '9':l+h}
    return function_hash[digit]


arabic_num = sys.argv[1]

length = len(arabic_num)
roman_num = 'M'*int(arabic_num[:-3]) if length > 3 else ''
roman_num += conversion('C', 'D', 'M', arabic_num[-3]) if length > 2 else ''
roman_num += conversion('X', 'L', 'C', arabic_num[-2]) if length > 1 else ''
roman_num += conversion('I', 'V', 'X', arabic_num[-1]) if length > 0 else ''

print(roman_num)
