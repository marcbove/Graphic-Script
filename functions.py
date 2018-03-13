#!/usr/bin/env python
# -*- coding: utf-8 -*-


from Tkinter import *
from tkFileDialog import *
import tkMessageBox 
import os, sys
from collections import defaultdict
import filecmp
import subprocess


def dirNameSrc(dir_NameSrc):
	dir_NameSrc.set(os.path.abspath(askdirectory()))


#Function dest
def dirNameDst(dir_NameDst):
	dir_NameDst.set(os.path.abspath(askdirectory()))

#Function 
def omplirDicc(fit_font, dir_NameSrc, dicc_fitx_ig, dicc_fitx_semb):
	for path, dirs, files in os.walk(dir_NameDst.get()):
		for f in files:
			if f.endswith('txt'):
				for fi in fit_font:
					if fi == f and filecmp.cmp(dir_NameSrc.get()+'/'+fi, path+'/'+f, shallow=False) and dir_NameSrc.get()!=path and path!='/home/milax/.local/share/Trash/files':
						dicc_fitx_ig[f].append(path+'/'+f)
					elif fi == f and dir_NameSrc.get()!=path:
						dicc_fitx_semb[f].append(path+'/'+f)

#Cerca de fitxers semblants
def dicIgual(dir_NameSrc, dir_NameDst, dicc_fitx_ig, dicc_fitx_semb, fit_or, lista_ig, lista_semb):
	try:
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
def seleccionar_tots(lista_or):
	if not lista_or.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista de ficheros originales")
	else:
		lista_or.selection_set(0, END)
	

#Función que deselecciona todos los ficheros originales de la lista
def deseleccionar_tots(lista_or):
	if not lista_or.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista de ficheros originales")
	else:
		lista_or.selection_clear(0, END)



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
def soft_link(lista_ig):
	if not lista_ig.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros iguales, la lista está vacía")
	else: 
		
		lista_ig_act_dest, lista_ig_act_src = listas()
		print lista_ig_act_dest
		p=subprocess.call(['/bin/sh','-c', './softlink.sh ',lista_ig_act_dest, lista_ig_act_src])
		#subprocess.call('./esborra.sh')

def hard_link(lista_ig):
	if not lista_ig.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros iguales, la lista está vacía")
	else: 
		lista_ig_act_dest, lista_ig_act_src = listas()
		subprocess.call('./hardlink.sh')


def esborra(lista_ig):
	if not lista_ig.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros en la lista")
	else: 
		subprocess.call('./esborraig.sh')


def renombra(lista_semb):
	if not lista_semb.get(0,END):
		tkMessageBox.showwarning("Warning", "No hay ficheros parecido, la lista está vacía")
	else: 
		subprocess.call('./esborraig.sh')
