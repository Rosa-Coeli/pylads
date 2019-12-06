#!/bin/bash

echo Insert integer in either roman or arabic numerals to get the other.
while :
do
	read input
	if [[ $input =~ ^[0-9]+$ ]]; then
		py ./05/Arabic_numerals_to_Roman.py $input
	elif [[ $input =~ ^-n[[:blank:]]+[MDCLXVImdclxvi]+$ ]]; then
		input=${input:3}
		arabic=$(py ./05/Roman_numerals_to_Arabic.py ${input^^})
		roman=$(py ./05/Arabic_numerals_to_Roman.py $arabic)
		echo Normalized roman numeral is probably $roman which equals $arabic.
	elif [[ $input =~ ^[IVXLCDM]+$ ]]; then
		py ./05/Roman_numerals_to_Arabic.py $input
	else	
		echo Just no.
	fi
done
