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
	echo -\'random\' to start playing random sequence of chords!
}



clear
sleep 3
commands

while :
do
	read menu_input
	case $menu_input in 
		exit | quit | x)
			break
			;;
		help)
			commands
			;;
		insert)
			./user_input.sh
			;;
		random)
			ret_value=$(py chord_initialisation.py)
			read
			./random_play.sh
			;;
	esac
done
echo $ret_value
