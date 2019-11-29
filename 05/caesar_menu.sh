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
	esac
	
done
