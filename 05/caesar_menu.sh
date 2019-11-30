#!/bin/bash

full_path=$(realpath $0)
dir_path=$(dirname $full_path)


commands () {
echo Welcome to ciphering service.
echo Type:
echo -\'exit\', \'quit\' or \'x\' to exit.
echo -\'help\' to show commands.
echo -\'caesar\' to begin ciphering in Caesar\'s cipher.
echo -\'morse '[<.> <_>]'\' to convert text to Morse code.
echo -\'snake\' to twist your text into a square spiral from an outer corner to the middle.
}


commands


while :
do
	read INPUT
	case $INPUT in
		exit | quit | x)
			break
			;;
		help)
			commands
			;;
		caesar | play)
			py $dir_path/Kaesar_cipher.py
			;;
		morse*)
			py $dir_path/Morse_code.py ${INPUT:5}
			;;
		snake)
			py $dir_path/snake.py
			;;
	esac
	
done
