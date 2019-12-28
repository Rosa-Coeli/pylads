#!/bin/bash


echo Zadej název akordu: 
read name

echo Zadej číslo pražce, od kterého akord začíná: 
read beginning

i=$beginning
while :
do
	echo Zadej bez mezer struny držené na pražci $i, až budeš hotov napiš \'0\': 
	read input
	if [[ $input == '0' ]]; then
		break
	fi
	strings[$i]=$input
	i=$(( i + 1 ))
done

echo Jsi si jistý, že chceš akord uložit? '(y/n)'
read save

while :
do
	case $save in
		y)
			all_strings=''
			for j in ${!strings[*]}
			do
				all_strings="$all_strings$j,${strings[$j]};"
			done
			echo $name:${all_strings%\;} >> $(dirname $(realpath $0))/chords.txt
			break
			;;
		n)
			break
			;;
		*)
	esac
done
