#!/bin/bash

dir_path=$(dirname $(realpath $0))


gap () {
	echo
	echo '		       ---    '
	echo
	read -t $wait_time random_play_input
}

wait_time=3

clear
sleep 3

gap

playlist=(G C)
num_playlist=${#playlist[*]}
while [[ $random_play_input != exit ]]
do
	cat .${playlist[$((RANDOM%num_playlist))]}.txt
	gap
done


#	previous_input_1=$previous_input_0
#	previous_input_0=$current_input
#	read current_input
#	input=$previous_input_1$previous_input_0$current_input
