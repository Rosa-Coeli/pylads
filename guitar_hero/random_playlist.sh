#!/bin/bash

dir_path=$(dirname $(realpath $0))

mkdir -p data/temp
read input_chord
while [[ $input_chord != '' ]]
do
	echo $input_chord >> $dir_path/data/temp/.playlist.txt
	read input_chord
done
