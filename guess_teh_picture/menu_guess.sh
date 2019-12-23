#!/bin/bash

dir_name=$(dirname $(realpath $0))

echo fraction: 
read fraction

for i in *.[Jj][Pp][Gg];
do
	py guess_the_picture.py $i $fraction
	read a
	read a
done
