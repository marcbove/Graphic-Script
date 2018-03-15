#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from tkFileDialog import *
import tkMessageBox 
import os, sys
from collections import defaultdict
import filecmp
import subprocess

dir_NameDst = ''
dir_NameSrc = ''
lista_ig = []
lista_semb = []
lista_x_act_src = [] 
lista_x_act_dest = []
lista_or = []
dicc_fitx_ig = {}
dicc_fitx_semb = {}

def dirName(name_dir):
	try:
		name_dir.set(os.path.abspath(askdirectory(title='Escoja un directorio', mustexist=1)))
	except AttributeError, e:
		pass
#Function 
def omplirDicc(fit_font):
	for path, dirs, files in os.walk(dir_NameDst.get()):
		for f in files:
			if f.endswith('txt'):
				a = f.replace(' ', '')
				for fi in fit_font:
					b = fi.replace(' ', '')
					if b == a and filecmp.cmp(dir_NameSrc.get()+'/'+fi, path+'/'+(f), shallow=False) and dir_NameSrc.get()!=path and path!='/home/milax/.local/share/Trash/files' and not os.path.islink(path+'/'+f):
						dicc_fitx_ig[fi].append(path+'/'+f)
					elif b == a and dir_NameSrc.get()!=path and not os.path.islink(path+'/'+f):
						dicc_fitx_semb[fi].append(path+'/'+f)

#Cerca de fitxers semblants
def dicIgual():
	try:
		fit_font = filter(lambda x: x.endswith('.txt'), os.listdir(dir_NameSrc.get()))
		asd = os.listdir(dir_NameDst.get())
		omplirDicc(fit_font)
		fit_or = filter(lambda fil: fil in dicc_fitx_ig.keys() or fil in dicc_fitx_semb.keys(), fit_font)

		for var in fit_or:
			lista_or.insert(END, var)
		
		llenarListas(lista_ig, dicc_fitx_ig)
		llenarListas(lista_semb, dicc_fitx_semb)

	except OSError, e:
		tkMessageBox.showerror("Error", "Introduzca directorios!")

#Funcio que omple segons una Listbox i un diccionari una de les ListBox
def llenarListas(lista, diccionario):
	for key, val in diccionario.iteritems():
			for i in val:
				lista.insert(END, '~/'+os.path.relpath(i, dir_NameSrc.get()))

#Funció que selecciona tots els fitxers de la llista passada per paràmetre
def seleccionar_tots(lista):
	if not lista.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista. Lista vacia!")
	else:
		lista.selection_set(0, END)
		
#Funció que deselecciona tots els fitxers de la llista passada per paràmetre
def deseleccionar_tots(lista):
	if not lista.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista. Lista vacia!")
	else:
		lista.selection_clear(0, END)

#Funció que omple les llistes necessàries per la GUI de compara
def llena_Listas(lista_inode, lista_path, lista_num):
	for val in lista_semb.curselection():
		lista_inode.insert(END, os.stat(os.path.abspath(lista_semb.get(val).replace('~/', ''))).st_ino) 
		lista_path.insert(END, lista_semb.get(val).replace('~/', ''))
			
	lista_num_dest, lista_num_src = listas_semb_ig(lista_semb, dicc_fitx_semb)

	for i in range(0, len(lista_num_dest)):
		with open(lista_num_dest[i], 'r') as dest:
			dest_array = dest.read().split('\n')
		with open(lista_num_src[i], 'r') as src:
			src_array = src.read().split('\n')				
		lista_num.insert(END,len(filter(lambda x: x not in src_array, dest_array)))
				
#listas para pasar por parametros 
def listas_semb_ig(lista, diccionari_fitxer):
	lista_x_act_dest = [lista.get(i) for i in lista.curselection()]
	lista_x_act_src = []
	for key, value in diccionari_fitxer.iteritems():
		for i in range(0, len(lista_x_act_dest)):
			elem_x = dir_NameDst.get()+lista_x_act_dest[i].replace('~', '')
			if elem_x in value:
				lista_x_act_src.append(key)
				lista_x_act_dest[i]=elem_x

	return lista_x_act_dest, lista_x_act_src

#Funció que linka segons el tipus que es passa per paràmetre
#Esborra de les estructures 
def link(type):
	if not lista_ig.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista. Lista vacia!")
	elif lista_ig.curselection() == ():
		tkMessageBox.showinfo("Information", "Selecciona alguno de los ficheros de la lista")
	else: 
		lista_ig_x_dest, lista_ig_x_src = listas_semb_ig(lista_ig, dicc_fitx_ig)
		esborra(lista_ig, dicc_fitx_ig)
		for i in range (0, len(lista_ig_x_dest)):
			if type == 'soft':
				os.symlink(dir_NameSrc.get()+'/'+lista_ig_x_src[i],lista_ig_x_dest[i])
				
			elif type == 'hard':
				os.link(dir_NameSrc.get()+'/'+lista_ig_x_src[i],lista_ig_x_dest[i])
			
			else:
				print 'Tipo no correcto'


#Esborra els fitxers seleccionats dels directoris, llistes i diccionaris
def esborra(lista, diccionari):
	if not lista.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista. Lista vacia!")
	elif lista.curselection() == ():
		tkMessageBox.showinfo("Information", "Selecciona alguno de los ficheros de la lista")
	else:
		#Obtenim les llistes amb tots els elements seleccionats (paths) de desti i font 
		lista_x_act_dest, lista_x_act_src = listas_semb_ig(lista, diccionari)
		#Per cada fitxer que esta activat en la llista es canvia el path pel complet, s'esborren els de desti de les carpetes, les listes i diccionaris
		for fitxer in lista_x_act_dest:
			fitxer=fitxer.replace('~',dir_NameDst.get())
			os.remove(fitxer)
			for key, value in diccionari.iteritems():
				if fitxer in value:
					diccionari[key].remove(fitxer)

		for elem_tupla in lista.curselection()[::-1]:
			lista.delete(elem_tupla)
		
#Renombra els fitxers activats de la llista de fitxers semblants canviant '.txt' per '(copia).txt'
#Esborra de la ListBox de fitxers semblants els fitxers als quals se'ls ha canviat el nom
def renombra():
	if not lista_semb.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista. Lista vacia!")
	elif lista_semb.curselection() == ():
		tkMessageBox.showinfo("Information", "Selecciona alguno de los ficheros de la lista")
	else: 
		for a in lista_semb.curselection():
			b=lista_semb.get(a)
			b=b.replace('~', dir_NameDst.get())
			os.rename(b, b.replace('.txt','(copia).txt'))
		for elem_tupla in lista_semb.curselection()[::-1]:	
			lista_semb.delete(elem_tupla)

#Función crea GUI compara
def compara_graf():
	if not lista_semb.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista. Lista vacia!")
	elif lista_semb.curselection() == ():
		tkMessageBox.showinfo("Information", "Selecciona alguno de los ficheros de la lista")
	else:
		ventanacomparacion = Toplevel()
		ventanacomparacion.minsize(500,200)
		ventanacomparacion.maxsize(500,200)

		#Creació de frames per les llistes d'inodes, path i el número de línies diferents
		fcomp = Frame(ventanacomparacion)
		finode = Frame(fcomp)
		fpath = Frame(fcomp)
		fnum = Frame(fcomp)

		#Creació de les labels inode, path i número de línies diferents
		linode = Label(finode, text = 'Inode:')
		lpath = Label(fpath, text = 'Path:')
		lnum = Label(fnum, text ='Num. Lín. Dif')

		#Creació de les scrollbars de les llistes de inodes, path i número de lín. dif. al seu frame 
		scrolInode = Scrollbar(finode, orient = VERTICAL)
		scrolpath = Scrollbar(fpath, orient = VERTICAL)
		scrolnum = Scrollbar(fnum, orient = VERTICAL)

		#Creació de les llistes (inodes, path, núm. lín. dif) al seu frame
		lista_inode = Listbox(finode, yscrollcommand = scrolInode.set)
		lista_path = Listbox(fpath, yscrollcommand = scrolpath.set)
		lista_num = Listbox(fnum, yscrollcommand = scrolnum.set)

		#Configuració de les scrollbars de les llistes
		scrolInode.config(command = lista_inode.yview)
		scrolpath.config(command = lista_path.yview)
		scrolnum.config(command = lista_num.yview)

		#Empaquetament de les estructures de Inode al seu frame
		linode.pack(side = TOP)
		lista_inode.pack(side = LEFT, expand = TRUE, fill = BOTH)
		scrolInode.pack(side = LEFT, fill = Y)

		#Empaquetament de les estructures de Path al seu frame
		lpath.pack(side = TOP)
		lista_path.pack(side = LEFT, expand = TRUE, fill = BOTH)
		scrolpath.pack(side = LEFT, fill = Y)

		#Empaquetament de les estructures de Núm. Lín. Dif al seu frame
		lnum.pack(side = TOP)
		lista_num.pack(side = LEFT, expand = TRUE, fill = BOTH)
		scrolnum.pack(side = LEFT, fill = Y)

		#Empaquetament dels frames
		finode.pack(side = LEFT, expand = TRUE, fill = BOTH)
		fpath.pack(side = LEFT, expand = TRUE, fill = BOTH)
		fnum.pack(side = LEFT, expand = TRUE, fill = BOTH)
		fcomp.pack(side = LEFT, expand = TRUE, fill = BOTH)

		#Omple les Listbox
		llena_Listas(lista_inode, lista_path, lista_num)

def sortir(window):
	if  tkMessageBox.askquestion('Sortir', "Segur que voleu sortir de l'aplicació?", icon= 'warning') == 'yes':
		window.quit()
		os.system('./src/destruccio_fitxers.sh')
