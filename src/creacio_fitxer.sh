#!/bin/bash
if [ $# -ne 1 ]; then 
	echo "Error! Introdueix el nom de l'script Python!"
	echo "exit 1"
	exit 1
fi
cd ..
mkdir -p Carp1/Carp1_1 Carp2 Carp3/Carp3_{1,2} Carp4/Carp4_1 Carp5/Carp5_{1,2}
echo -e "\nDirectoris creats!\nFitxers i directoris:"
ls
A="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
\nlabore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris
\nnisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit
\nesse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in
\nculpa qui officia deserunt mollit anim id est laborum."
B="Sed ut perspiciatis unde omnis iste natus error sit voluptatem accusantium doloremque laudantium,
\ntotam rem aperiam, eaque ipsa quae ab illo inventore veritatis et quasi architecto beatae vitae dicta sunt
\nexplicabo. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur
\nmagni dolores eos qui ratione voluptatem sequi nesciunt. Neque porro quisquam est, qui dolorem ipsum quia dolor
\nsit amet, consectetur, adipisci velit, sed quia non numquam eius modi tempora incidunt ut labore et dolore magnam
\naliquam quaerat voluptatem. Ut enim ad minima veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam,
\nnisi ut aliquid ex ea commodi consequatur? Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam
\nnihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
C="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut
\nlabore et dolore magna aliqua. Nemo enim ipsam voluptatem quia voluptas sit aspernatur aut odit aut fugit, sed quia consequuntur
\nmagni dolores eos qui ratione voluptatem sequi nesciunt. Duis aute irure dolor in reprehenderit in voluptate velit
\nesse cillum dolore eu fugiat nulla pariatur. Quis autem vel eum iure reprehenderit qui in ea voluptate velit esse quam
\nnihil molestiae consequatur, vel illum qui dolorem eum fugiat quo voluptas nulla pariatur?"
cd Carp4
echo -e $B > "ipsum.txt"
echo -e $B > "lorem.txt"
echo -e $C > "remsum.txt"
cd Carp4_1
echo -e $B > "ipsum.txt"
echo -e $C > "lorem.txt"
echo -e $B > "i psum.txt"
echo -e $C > "remsum.txt"
cd ..
cd ..
cd Carp5
echo -e $B > "remsum.txt"
echo -e $A > "ipsum.txt"
cd Carp5_1
echo -e $B > "ipsum.txt"
echo -e $B > "remsum.txt"
echo -e $B > "lorem.txt"
echo -e $A > "ipsum.txt"
echo -e $C > "lorem.txt"
echo -e $B > "ipsum.txt"
cd ..
cd Carp5_2
echo -e $A > "lorem.txt"
echo -e $C > "ipsum.txt"
echo -e $A > "ipsum.txt"
echo -e $B > "i psum.txt"
cd ..
cd ..
echo -e $A > "lorem.txt"
echo -e $B > "ipsum.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll10.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll11.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll12.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll13.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll14.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll15.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll16.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll17.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll18.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll19.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll20.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll21.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll22.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll23.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll24.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll25.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll26.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll27.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll28.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll29.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll30.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll31.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll32.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll33.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll34.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll35.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll36.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll37.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll38.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll39.txt"
cd Carp1/
#echo -e $A > "lorem.txt"
#echo -e $C > "ipsum.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll10.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll11.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll12.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll13.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll14.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll15.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll16.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll17.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll18.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll19.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll20.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll21.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll22.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll23.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll24.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll25.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll26.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll27.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll28.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll29.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll30.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll31.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll32.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll33.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll34.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll35.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll36.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll37.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll38.txt"
#echo -e "Provar que l'scrollbar va be" > "prova_scroll39.txt"
cd Carp1_1/
echo -e $B > "ipsum.txt"
echo -e $B > "ipsum.txt"
echo -e $B > "lorem.txt"
echo -e $B > "i psum.txt"
echo -e $B > "remsum.txt"
cd ..
cd ..
cd Carp2/
echo -e $B > "lorem.txt"
echo -e $A > "ipsum.txt"
echo -e $A > "remsum.txt"
cd ..
cd Carp3/
echo -e $C > "lorem.txt"
echo -e $B > "ipsum.txt"
cd Carp3_1/
echo -e $B > "i psum.txt"
echo -e $C > "lor em.txt"
echo -e $C > "remsum.txt"
cd ..
cd Carp3_2/
echo -e $A > "lorem.txt"
echo -e $C > "remsum.txt"
echo -e $A > "ipsum.txt"
echo -e $C > "remsum.txt"
cd ..
cd ..
echo -e "\nFitxers Creats!\n"
./src/$1
exit 0
