#!/bin/bash
mkdir -p first{0..2}/second{0..2}/third{0..2}
echo "Directoris creats!"
text=(zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen)
i=0
for file in {g..m}
do
	echo text[0] > "$file.txt"
	let i+1
done
cd first0/
i=0
for file in {g..f}
do
	echo text[i] > "$file.txt"
	let i+1
done
cd second0/
for file in {k..m}
do
	echo text[i] > "$file.txt"
	let i+1
done
cd ..
cd second1/
i=0
for file in {k..m}
do
	echo text[i] > "$file.txt"
	let i+1
done
cd ..
cd ..
cd first1/
i=0
for file in {g..m}
do
	echo text[i] > "$file.txt"
	let i+1
done
cd second0/
for file in {f..k}
do
	echo text[i] > "$file.txt"
	let i+1
done
cd ..
i=0
cd second1/
for file in {i..l}
do
	echo text[i] > "$file.txt"
	let i+1
done
echo "Fitxers Creats!"
