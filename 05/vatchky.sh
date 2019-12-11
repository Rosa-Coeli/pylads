#!/bin/bash

i=0
clear
for _ in {0,3}
do
	echo
done
sleep 10

while :
do
	while [[  10 -gt $i ]]
	do
		i=$i+1
		echo Vačky.
		echo
		sleep 5
		echo Hej, Vačky!
		echo
		sleep 5
	done
	i=0
	echo
	echo Vaaaaaaaaaaaaačččččkýýýýýýýýýýýýýý!!!!!!!
	sleep 2
	echo Pracuj!
	sleep 5
	echo
done
