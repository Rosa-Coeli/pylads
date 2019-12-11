#!/bin/bash

dir_name=$(dirname $(realpath $0))

echo Insert integer in either roman or arabic numerals to get the other.
while :
do
	read input
	if [[ $input =~ ^[0-9]+$ ]]; then
		py $dir_name/05/Arabic_numerals_to_Roman.py $input
	elif [[ $input =~ ^-n[[:blank:]]+[MDCLXVImdclxvi]+$ ]]; then
		input=${input:3}
		arabic=$(py $dir_name/05/Roman_numerals_to_Arabic.py ${input^^})
		roman=$(py $dir_name/05/Arabic_numerals_to_Roman.py $arabic)
		echo Normalized roman numeral is probably $roman which equals to $arabic.
	elif [[ $input =~ ^[IVXLCDMivxlcdm]+$ ]]; then
		py $dir_name/05/Roman_numerals_to_Arabic.py ${input^^}
	elif [[ $input =~ exit|quit ]]; then
		break
	else	
		echo Just no.
	fi
done
