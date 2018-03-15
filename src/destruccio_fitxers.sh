#!/bin/bash
cd ..
echo -e "\nFitxers abans d'eliminar:"
ls
#-r recursivo, -f para que no le importe si no existe
rm -r -f Carp1
rm -r -f Carp2 
rm -r -f Carp3
rm -f ipsum.txt
rm -f lorem.txt
echo -e "\nDirectoris esborrats!\n\nFitxers i directoris:"
ls
echo ""