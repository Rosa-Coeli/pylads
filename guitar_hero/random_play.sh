#!/bin/bash

dir_path=$(dirname $(realpath $0))


gap () {
	echo
	echo '		       ---    '
	echo
	read -t $wait_time random_play_input
}

wait_time=3

#clear

gap


playlist=(G C A D F E Ami Emi Dmi Cmi Gmi G\# G\#mi Amaj7 H6/9 C\#maj9 A\#mi9 Edim7 G13 D\#sus)
num_playlist=${#playlist[*]}
while [[ $random_play_input != exit ]]
do
	cat ./data/temp/.${playlist[$((RANDOM%num_playlist))]}.txt
	gap
done


#	previous_input_1=$previous_input_0
#	previous_input_0=$current_input
#	read current_input
#	input=$previous_input_1$previous_input_0$current_input
