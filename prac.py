#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from tkFileDialog import *
import tkMessageBox 
import os, sys
from collections import defaultdict
import filecmp
import subprocess
#from functions import *


#Create window
window=Tk()
window.title("Cerca fitxers Redundants")
window.minsize(500,450)
window.maxsize(500,450)

#Variables
dir_NameDst = StringVar()
dir_NameSrc = StringVar()
dicc_fitx_ig = defaultdict(list)
dicc_fitx_semb = defaultdict(list)
fit_desti = Listbox()

#Function source
def dirNameSrc():
	dir_NameSrc.set(os.path.abspath(askdirectory()))

#Function dest
def dirNameDst():
	dir_NameDst.set(os.path.abspath(askdirectory()))

#Function 
def omplirDicc(fit_font):
	for path, dirs, files in os.walk(dir_NameDst.get()):
		for f in files:
			if f.endswith('txt'):
				for fi in fit_font:
					if fi == f and filecmp.cmp(dir_NameSrc.get()+'/'+fi, path+'/'+f, shallow=False) and dir_NameSrc.get()!=path and path!='/home/milax/.local/share/Trash/files' and not os.path.islink(path+'/'+f):
						dicc_fitx_ig[f].append(path+'/'+f)
					elif fi == f and dir_NameSrc.get()!=path and path!='/home/milax/.local/share/Trash/files' and not os.path.islink(path+'/'+f):
						dicc_fitx_semb[f].append(path+'/'+f)
	print 'semb', dicc_fitx_semb
	print 'ig', dicc_fitx_ig

#Cerca de fitxers semblants
def dicIgual():
	try:
		print 'directorios', dir_NameDst.get(), dir_NameSrc.get()
		print 'diccionarios', dicc_fitx_ig, dicc_fitx_semb
		fit_font = filter(lambda x: x.endswith('.txt'), os.listdir(dir_NameSrc.get()))
		asd = os.listdir(dir_NameDst.get())
		omplirDicc(fit_font)
		fit_or = filter(lambda fil: fil in dicc_fitx_ig.keys() or fil in dicc_fitx_semb.keys(), fit_font)

		for var in fit_or:
			lista_or.insert(END, var)

		for key, val in dicc_fitx_ig.iteritems():
			for i in val:
				lista_ig.insert(END, '~/'+os.path.relpath(i, dir_NameSrc.get()))

		for key, val in dicc_fitx_semb.iteritems():
			for i in val:
				lista_semb.insert(END, '~/'+os.path.relpath(i, dir_NameSrc.get()))

	except OSError, e:
		tkMessageBox.showerror("Error", "Introduzca directorios")
		

#Función que selecciona todos los ficheros originales de la lista
def seleccionar_tots_or():
	if not lista_or.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista de ficheros originales")
	else:
		lista_or.selection_set(0, END)
	

#Función que selecciona todos los ficheros iguales de la lista
def seleccionar_tots_ig():
	if not lista_ig.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista de ficheros iguales")
	else:
		lista_ig.selection_set(0, END)


#Función que selecciona todos los ficheros semblants de la lista
def seleccionar_tots_semb():
	if not lista_semb.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista de ficheros parecidos")
	else:
		lista_semb.selection_set(0, END)

#Función que deselecciona todos los ficheros originales de la lista
def deseleccionar_tots_or():
	if not lista_or.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista de ficheros originales")
	else:
		lista_or.selection_clear(0, END)

#Función que deselecciona todos los ficheros iguales de la lista
def deseleccionar_tots_ig():
	if not lista_ig.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista de ficheros iguales")
	else:
		lista_ig.selection_clear(0, END)

#Función que deselecciona todos los ficheros semblants de la lista
def deseleccionar_tots_semb():
	if not lista_semb.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista de ficheros parecidos")
	else:
		lista_semb.selection_clear(0, END)

#Función crea GUI compara
def compara_graf():
	if not lista_semb.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros parecidos")
	else:
		ventanacomparacion = Toplevel()
		ventanacomparacion.minsize(500,200)
		ventanacomparacion.maxsize(500,200)

		fcomp = Frame(ventanacomparacion)
		finode = Frame(fcomp)
		fpath = Frame(fcomp)
		fnum = Frame(fcomp)

		linode = Label(finode, text = 'Inode:')
		lpath = Label(fpath, text = 'Path:')
		lnum = Label(fnum, text ='Num. Lín. Dif')

		scrolInode = Scrollbar(finode, orient = VERTICAL)
		scrolpath = Scrollbar(fpath, orient = VERTICAL)
		scrolnum = Scrollbar(fnum, orient = VERTICAL)

		lista_inode = Listbox(finode, yscrollcommand = scrolInode.set)
		lista_path = Listbox(fpath, yscrollcommand = scrolpath.set)
		lista_num = Listbox(fnum, yscrollcommand = scrolnum.set)

		scrolInode.config(command = lista_inode.yview)
		scrolpath.config(command = lista_path.yview)
		scrolnum.config(command = lista_num.yview)

		linode.pack(side = TOP)
		lista_inode.pack(side = LEFT, expand = TRUE, fill = BOTH)
		scrolInode.pack(side = LEFT, fill = Y)

		lpath.pack(side = TOP)
		lista_path.pack(side = LEFT, expand = TRUE, fill = BOTH)
		scrolpath.pack(side = LEFT, fill = Y)

		lnum.pack(side = TOP)
		lista_num.pack(side = LEFT, expand = TRUE, fill = BOTH)
		scrolnum.pack(side = LEFT, fill = Y)

		finode.pack(side = LEFT, expand = TRUE, fill = BOTH)
		fpath.pack(side = LEFT, expand = TRUE, fill = BOTH)
		fnum.pack(side = LEFT, expand = TRUE, fill = BOTH)
		fcomp.pack(side = LEFT, expand = TRUE, fill = BOTH)

		llena_Listas(lista_inode, lista_path)


#Función crea GUI compara
def llena_Listas(lista_inode, lista_path):
	for val in lista_semb.curselection():
		lista_inode.insert(END, os.stat(os.path.abspath(lista_semb.get(val).replace('~/', ''))).st_ino) 
		lista_path.insert(END, lista_semb.get(val).replace('~/', ''))



#listas para pasar por parametros 
def listas():
	lista_ig_act_dest = [lista_ig.get(i) for i in lista_ig.curselection()]
	lista_ig_act_src = []
	for key, value in dicc_fitx_ig.iteritems():
		for elem in lista_ig_act_dest:
			elem_x = dir_NameDst.get()+elem.replace('~', '')
			if elem_x in value:
				lista_ig_act_src.append(key)
				lista_ig_act_dest.append(elem_x)
	
	index=0
	for i in range(0, len(lista_ig_act_dest)):
		if lista_ig_act_dest[0].startswith('~'):
			del lista_ig_act_dest[0]
		if i==len(lista_ig_act_dest)/2:
			break
	return lista_ig_act_dest, lista_ig_act_src


#Soft Link
def soft_link():
	if not lista_ig.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros iguales, la lista está vacía")
	else: 
		lista_ig_act_dest, lista_ig_act_src = listas()
		esborra(lista_ig_act_dest)
		print len(lista_ig_act_dest), len(lista_ig_act_src)
		for i in range (0, len(lista_ig_act_dest)):
			os.symlink(dir_NameSrc.get()+'/'+lista_ig_act_src[i],lista_ig_act_dest[i])

def hard_link():
	if not lista_ig.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros iguales, la lista está vacía")
	else: 
		lista_ig_act_dest, lista_ig_act_src = listas()
		esborra(lista_ig_act_dest)
		print len(lista_ig_act_dest), len(lista_ig_act_src)
		for i in range (0, len(lista_ig_act_dest)):
			os.link(dir_NameSrc.get()+'/'+lista_ig_act_src[i],lista_ig_act_dest[i])
		

def esborra(lista):
	if not lista_ig.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista")
	else: 
		print 'esborra', lista
		for fitxer in lista:
			os.remove(fitxer)


def renombra():
	if not lista_semb.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros parecido, la lista está vacía")
	else: 
		print lista_semb.get(0,END)
		lista_ig_act_dest, lista_ig_act_src = listas()
		for a in lista_ig_act_dest:
			os.rename(a, str(a)+'copia')

#GUI's First Line: ask origin directory

fDirectFont = Frame(window)
#lambda: dirNameSrc(dir_NameSrc)
bDirectFont = Button(fDirectFont, text = 'Escolliu directori font', command = dirNameSrc)
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
#lambda: seleccionar_tots_or(lista_or)
#lambda: deseleccionar_tots_or(lista_or)
bTots = Button(fSelecciona, text = 'Selecciona Tots', command = seleccionar_tots_or)
bCap = Button(fSelecciona, text = 'Selecciona Cap', command = deseleccionar_tots_or)



#GUI's Second Line: ask destination directory and search
fDirectDest = Frame(window)
#lambda: dirNameDst(dir_NameDst)
bDirectDest = Button(fDirectDest, text = 'Escolliu directori destí', command = dirNameDst)
lDirectDest = Label(fDirectDest, textvariable = dir_NameDst, relief = "sunken")
#lambda: dicIgual(dicc_fitx_ig)
bCerca = Button(fDirectDest, text = 'Cerca', command = dicIgual)



bDirectDest.pack(side = LEFT)
lDirectDest.pack(side = LEFT, expand = TRUE, fill = X)
bCerca.pack(side = LEFT)

#GUI's last line: exit button
fSortir = Frame(window)
bSortir = Button(fSortir, text = 'Sortir', command = window.quit)

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
lista_ig.pack(side = RIGHT, expand = TRUE, fill = X)

#Iguals' Buttons
fFitxIgualButton = Frame(fIguals)
bEsborra = Button(fFitxIgualButton, text = 'Esborra', command = lambda: esborra(lista_semb))
bHLink = Button(fFitxIgualButton, text = 'Hard Link', command = hard_link)
bSLink = Button(fFitxIgualButton, text = 'Soft Link', command = soft_link)
bSelecTotsA = Button(fFitxIgualButton, text = 'Selec Tots', command = seleccionar_tots_ig)
bSelecCapA = Button(fFitxIgualButton, text = 'Selec Cap', command = deseleccionar_tots_ig)

bEsborra.pack(side = TOP, anchor = W)				
bHLink.pack(side = TOP, anchor = W)				
bSLink.pack(side = TOP, anchor = W)				
bSelecTotsA.pack(side = TOP, anchor = W)				
bSelecCapA.pack(side = TOP, anchor = W)
fIgualScroll.pack(side = LEFT)
fFitxIgualButton.pack(side = LEFT)
fIguals.pack(side = TOP, expand = TRUE, fill = X)

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
lista_semb.pack(side = RIGHT, expand = TRUE, fill = X)
			
#GUI's buttons for 'Fitxers Semblants'
fFitxSemblButton = Frame(fSembl)
bCompara = Button(fFitxSemblButton, text = 'Compara', command = compara_graf)
bRenombra = Button(fFitxSemblButton, text = 'Renombra', command = lambda: renombra())
bEsborra = Button(fFitxSemblButton, text = 'Esborra', command = lambda: esborra(lista_semb))
bSelecTotsB = Button(fFitxSemblButton, text = 'Selec Tots', command = seleccionar_tots_semb)
bSelecCapB = Button(fFitxSemblButton, text = 'Selec Cap', command = deseleccionar_tots_semb)

bCompara.pack(side = TOP, anchor = W)
bRenombra.pack(side = TOP, anchor = W)
bEsborra.pack(side = TOP, anchor = W)
bSelecTotsB.pack(side = TOP, anchor = W)
bSelecCapB.pack(side = TOP, anchor = W)

fSemblScroll.pack(side = LEFT)
fFitxSemblButton.pack(side = LEFT)
fSembl.pack(side = TOP, expand = TRUE, fill = X)

#Pack frames
fDirectFont.pack(side = TOP, expand = TRUE, fill = X)
fDirectDest.pack(side = TOP, expand = TRUE, fill = X)
fSortir.pack(side = BOTTOM, expand = TRUE, fill = X)
fSelecciona.pack(side = BOTTOM, expand = TRUE, fill = X)
fOriginals.pack(side = LEFT, expand = TRUE, fill = BOTH)
fIgualSembl.pack(side = LEFT, expand = TRUE, fill = X)
fFitxers.pack(side = LEFT, expand = TRUE, fill = X)

window.mainloop()
