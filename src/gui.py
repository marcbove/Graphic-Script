#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from tkFileDialog import *
from collections import defaultdict
import functions as func

#Create window
window=Tk()
window.title("Cerca fitxers Redundants")
window.minsize(500,500)
window.maxsize(999,500)

#Variables
dir_NameDst = StringVar()
dir_NameSrc = StringVar()
dicc_fitx_ig = defaultdict(list)
dicc_fitx_semb = defaultdict(list)

fDirectFont = Frame(window)
bDirectFont = Button(fDirectFont, text = 'Escolliu directori font', command = lambda: func.dirName(dir_NameSrc))
lDirectFont = Label(fDirectFont, textvariable = dir_NameSrc, relief = "sunken")

bDirectFont.pack(side = LEFT)
lDirectFont.pack(side = LEFT, expand = TRUE, fill = X)

#Frame for GUI's scrollboxes
fFitxers = Frame(window)

#GUI's frame for Originals scrollbox
fOriginals = Frame(fFitxers)
lOriginals = Label(fOriginals, text = 'Fitxers Originals:')
scrolOriginal = Scrollbar(fOriginals, orient = VERTICAL)
lista_or = Listbox(fOriginals, yscrollcommand = scrolOriginal.set, selectmode = 'multiple')
scrolOriginal.config(command = lista_or.yview)

#GUI's second-to-last: selecciona tots/cap
fSelecciona = Frame(window)
bTots = Button(fSelecciona, text = 'Selecciona Tots', command = lambda: func.seleccionar_tots_or(lista_or))
bCap = Button(fSelecciona, text = 'Selecciona Cap', command = lambda: func.deseleccionar_tots_or(lista_or))

#GUI's Second Line: ask destination directory and search
fDirectDest = Frame(window)
bDirectDest = Button(fDirectDest, text = 'Escolliu directori destí', command = lambda: func.dirName(dir_NameDst))
lDirectDest = Label(fDirectDest, textvariable = dir_NameDst, relief = "sunken")

bCerca = Button(fDirectDest, text = 'Cerca', command = lambda: func.dicIgual())

bDirectDest.pack(side = LEFT)
lDirectDest.pack(side = LEFT, expand = TRUE, fill = X)
bCerca.pack(side = LEFT)

fOrdenar = Frame(window)
bOrdenar = Button(fOrdenar, text = 'Ordenar', command = lambda: func.ordenar(lista_or, lista_ig, lista_semb))

#GUI's last line: exit button
fSortir = Frame(window)
bSortir = Button(fSortir, text = 'Sortir', command = lambda: func.sortir(window))

bOrdenar.pack(side = LEFT)
bSortir.pack(side = LEFT)

bTots.pack(side = LEFT)
bCap.pack(side = LEFT)

lOriginals.pack(side = TOP, anchor = W)
scrolOriginal.pack(side = RIGHT, fill = Y)
lista_or.pack(side = LEFT, expand = TRUE, fill = BOTH)

#GUI's frame for Iguals i Semblants
fIgualSembl = Frame(fFitxers)

#GUI's frame for Iguals
fIguals = Frame(fIgualSembl)
lIguals = Label(fIguals, text = '    Fitxers Iguals:')

lIguals.pack(side = TOP, anchor = W)

#Iguals' Scrollbox
fIgualScroll = Frame(fIguals)
scrollIguals = Scrollbar(fIgualScroll, orient = VERTICAL)
lista_ig = Listbox(fIgualScroll, yscrollcommand = scrollIguals.set, selectmode = 'multiple')
scrollIguals.config(command = lista_ig.yview)

scrollIguals.pack(side = LEFT, fill = Y)
lista_ig.pack(side = RIGHT, expand = TRUE, fill = BOTH)

#Iguals' Buttons
fFitxIgualButton = Frame(fIguals)
bEsborra = Button(fFitxIgualButton, text = 'Esborra', command = lambda: func.esborra(lista_ig, dicc_fitx_ig))
bHLink = Button(fFitxIgualButton, text = 'Hard Link', command = lambda: func.link('hard'))
bSLink = Button(fFitxIgualButton, text = 'Soft Link', command = lambda: func.link('soft'))
bSelecTotsA = Button(fFitxIgualButton, text = 'Selec Tots', command = lambda: func.seleccionar_tots(lista_ig))
bSelecCapA = Button(fFitxIgualButton, text = 'Selec Cap', command = lambda: func.deseleccionar_tots(lista_ig))

bEsborra.pack(side = TOP, fill = X)				
bHLink.pack(side = TOP, fill = X)				
bSLink.pack(side = TOP, fill = X)				
bSelecTotsA.pack(side = TOP, fill = X)				
bSelecCapA.pack(side = TOP, fill = X)
fIgualScroll.pack(side = LEFT, expand = TRUE, fill = BOTH)
fFitxIgualButton.pack(side = LEFT)
fIguals.pack(side = TOP, expand = TRUE, fill = BOTH)

#GUI's frame for Semblants
fSembl = Frame(fIgualSembl)
lSembl = Label(fSembl, text = '    Fitxers Semblants')

lSembl.pack(side = TOP, anchor = W)

#Semblants' ScrollBox
fSemblScroll = Frame(fSembl)
scrollSembl = Scrollbar(fSemblScroll, orient = VERTICAL)
lista_semb = Listbox(fSemblScroll, yscrollcommand = scrollSembl.set, selectmode = 'multiple')
scrollSembl.config(command = lista_semb.yview)

scrollSembl.pack(side = LEFT, fill = Y)
lista_semb.pack(side = RIGHT, expand = TRUE, fill = BOTH)
			
#GUI's buttons for 'Fitxers Semblants'
fFitxSemblButton = Frame(fSembl)
bCompara = Button(fFitxSemblButton, text = 'Compara', command = lambda: func.compara_graf())
bRenombra = Button(fFitxSemblButton, text = 'Renombra', command = lambda: func.renombra())
bEsborra = Button(fFitxSemblButton, text = 'Esborra', command = lambda: func.esborra(lista_semb, dicc_fitx_semb))
bSelecTotsB = Button(fFitxSemblButton, text = 'Selec Tots', command = lambda: func.seleccionar_tots(lista_semb))
bSelecCapB = Button(fFitxSemblButton, text = 'Selec Cap', command = lambda: func.deseleccionar_tots(lista_semb))

bEsborra.pack(side = TOP, fill = X)
bCompara.pack(side = TOP, fill = X)
bRenombra.pack(side = TOP, fill = X)
bSelecTotsB.pack(side = TOP, fill = X)
bSelecCapB.pack(side = TOP, fill = X)
			
fSemblScroll.pack(side = LEFT, expand = TRUE, fill = BOTH)
fFitxSemblButton.pack(side = LEFT)
fSembl.pack(side = TOP, expand = TRUE, fill = BOTH)

#Pack frames
fDirectFont.pack(side = TOP, expand = TRUE, fill = X)
fDirectDest.pack(side = TOP, expand = TRUE, fill = X)
fSortir.pack(side = BOTTOM, expand = TRUE, fill = X)
fOrdenar.pack(side = BOTTOM, expand = TRUE, fill = X)
fSelecciona.pack(side = BOTTOM, expand = TRUE, fill = X)
fOriginals.pack(side = LEFT, expand = TRUE, fill = BOTH)
fIgualSembl.pack(side = LEFT, expand = TRUE, fill = BOTH)
fFitxers.pack(side = LEFT, expand = TRUE, fill = BOTH)

func.dir_NameDst = dir_NameDst
func.dir_NameSrc = dir_NameSrc
func.dicc_fitx_ig = dicc_fitx_ig
func.dicc_fitx_semb = dicc_fitx_semb
func.lista_ig = lista_ig
func.lista_semb = lista_semb
func.lista_or = lista_or

lista_or.bind('<<ListboxSelect>>', func.onselect)


window.mainloop()
