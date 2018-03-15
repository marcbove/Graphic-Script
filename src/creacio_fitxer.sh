#!/bin/bash
if [ $# -ne 1 ]; then 
	echo "Error! Introdueix el nom de l'script Python!"
	echo "exit 1"
	exit 1
fi
cd ..
mkdir -p Carp1/Carp1_1 Carp2 Carp3/Carp3_{1,2}
echo -e "\nDirectoris creats!\nFitxers i directoris:"
ls
#mkdir -p Carp2
#mkdir -p Carp3/Carp31
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
echo -e $A > "lorem.txt"
echo -e $B > "ipsum.txt"
cd Carp1/
echo -e $A > "lorem.txt"
echo -e $C > "ipsum.txt"
cd Carp1_1/
echo -e $B > "ipsum.txt"
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
cd ..
cd ..
echo -e "\nFitxers Creats!\n"
./src/$1
exit 0