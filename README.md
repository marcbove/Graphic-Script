# Graphic Scripts

En aquesta pràctica volem fer una aplicació gràfica que busqui rèpliques de tots els arxius
locals d’un directori font (sense subdirectoris) a un arbre de directoris destí. Els que trobi que
coincideixen en el nom, caldrà comprovar-los en contingut per a saber si són iguals o si hi ha
diferències en el contingut.
A continuació es mostra una captura de la interfície gràfica implementada juntament amb una
breu descripció de les funcionalitats implementades:

![Exemple de la inferfície gràfica](https://)

- *Escollir directori font*: Permet escollir el directori font per iniciar la comparació,
només mirarem els fitxers que estan directament sota aquest directori.
- *Escollir directori destí*: Permet escollir el directori destí on s’ha de mirar si hi ha
coincidències de fitxers amb els del directori font.
- *Llista fitxers originals*: contindrà la llista dels fitxers del directori font, el nom dels
quals també estan en el directori destí.
- *Llista fitxers iguals*: contindrà el path relatiu al directori destí dels fitxers que són
iguals (nom i contingut) als del directori font seleccionat.
- *Llista fitxers semblants*: contindrà el path relatiu al directori destí dels fitxers que són
semblants (tenen el mateix nom però el contingut té diferències) als del directori font
seleccionat.
- *Cerca*: Executa l’script que fa la cerca de les rèpliques i omple les tres llistes: els
originals (fitxers dels que n’ha trobat una còpia), la llista de fitxers que s’han trobat
idèntics a algun original i la llista de fitxers que són semblants a algun original.
- *Selecciona Tots*: selecciona tots els fitxers de la llista propera al botó que premem.
- *Selecciona Cap*: deselecciona tots els fitxers de la llista propera al botó que premem.
- *Esborra*: esborra els fitxers seleccionats de la llista més propera.
- *Sortir*: Finalitza l'aplicació.

A més a més de les opcions anteriors, pels fitxers iguals donarem a l’usuari les opcions:
- *Hard Link*: per a cada fitxer igual seleccionat, el substitueix per un hard-link a
l’original.
- *Soft Link*: per a cada fitxer igual seleccionat, el substitueix per un soft-link a l’original.

Mentre que pels fitxers que tenen igual nom però que són diferents permetrem que l’usuari:
- *Compara*: compara els fitxers seleccionats mostrant en una subfinestra l’inode i path
relatiu al directori destí de cadascun dels fitxers iguals i el nombre de línies diferents.
Opcionalment, també, pot obrir una finestra per a comparar/modificar els fitxers, de
dos en dos (original i rèplica) amb el vimdiff o el gvimdiffs
- *Renombra*: re-nombra els fitxer del directori destí fent que el nom del fitxer del
directori destí comenci per un substring demanat a l’usuari.

Llenguatges utilitzats: Shell-scripts, programació de l’intèrpret de comandes UNIX, el llenguatge 
de programació Python i la seva extensió TkInter per a crear scripts gràfics.

Subject: FSO (Foundations of Operating Systems)

Authors: Gwen Mege & Marc Bové
