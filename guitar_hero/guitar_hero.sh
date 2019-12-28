#!/bin/bash


dir_path=$(dirname $(realpath $0))


echo -n Write how many seconds of time you want inbetween chords: 
read wait_time


gap () {
	echo
	echo '		       ---    '
	echo
	sleep $wait_time
}


commands () {
	echo Welcome to the Guitar Realo.
	echo Type:
	echo -\'exit\', \'quit\' or \'x\' to exit.
	echo -\'help\' to show commands.
	echo -\'insert\' to insert new chords.
	echo -\'play\' to start playing!
}



clear
sleep 3

while :
do
	read input
	case $input in 
		exit | quit | x)
			break
			;;
		help)
			commands
			;;
		insert)
			./user_input.sh
			;;
		play)
			;;
	esac
done
