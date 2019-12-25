#!/bin/bash

dir_name=$(dirname $(realpath $0))

for i in {1..18}
do
	roman=$(py $dir_name/../05/Arabic_numerals_to_Roman.py $i)
	echo Kapitosela $roman. >> Babicka_sele.txt
	echo >> Babicka_sele.txt
	echo >> Babicka_sele.txt
	cat $roman.txt >> Babicka_sele.txt 
	echo >> Babicka_sele.txt
	echo >> Babicka_sele.txt
done
