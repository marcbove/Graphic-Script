#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Tkinter import *
from tkFileDialog import *
import tkMessageBox 
import os, sys
from collections import defaultdict
import filecmp
import subprocess

class GUI:
	dir_NameDst = ''
	dir_NameSrc = ''
	dicc_fitx_ig = {}
	dicc_fitx_semb = {}
	lista_ig = [] 
	lista_semb = [] 
	lista_ig_act_src = [] 
	lista_ig_act_dest = []

	def __init__(self, dir_NameDst, dir_NameSrc, dicc_fitx_ig, dicc_fitx_semb, lista_ig, lista_semb):
		self.dir_NameDst = dir_NameDst
		self.dir_NameSrc = dir_NameSrc
		self.dicc_fitx_ig = dicc_fitx_ig
		self.dicc_fitx_semb = dicc_fitx_semb
		self.lista_ig = lista_ig
		self.lista_semb = lista_semb
		lista_ig_act_src = [] 
		lista_ig_act_dest = []

	def dirName(self, name_dir):
		name_dir.set(os.path.abspath(askdirectory()))

	#Function 
	def omplirDicc(self, fit_font, dir_NameSrc, dir_NameDst):
		for path, dirs, files in os.walk(dir_NameDst.get()):
			for f in files:
				if f.endswith('txt'):
					for fi in fit_font:
						if fi == f and filecmp.cmp(dir_NameSrc.get()+'/'+fi, path+'/'+f, shallow=False) and dir_NameSrc.get()!=path and path!='/home/milax/.local/share/Trash/files':
							dicc_fitx_ig[f].append(path+'/'+f)
						elif fi == f and dir_NameSrc.get()!=path:
							dicc_fitx_semb[f].append(path+'/'+f)

	#Cerca de fitxers semblants
	def dicIgual(self, dir_NameSrc, dir_NameDst):
		try:
			fit_font = filter(lambda x: x.endswith('.txt'), os.listdir(dir_NameSrc.get()))
			asd = os.listdir(dir_NameDst.get())
			self.omplirDicc(fit_font, dir_NameSrc, dir_NameDst)
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
	def seleccionar_tots(self, lista):
		if not lista.get(0,END):
			tkMessageBox.showwarning("Warning", "No hay ficheros en la lista!")
		else:
			lista.selection_set(0, END)
		
	#Función que deselecciona todos los ficheros originales de la lista
	def deseleccionar_tots(self, lista):
		if not lista.get(0,END):
			tkMessageBox.showwarning("Warning", "No hay ficheros en la lista!")
		else:
			lista.selection_clear(0, END)

	#Función crea GUI compara
	def llena_Listas(self, lista_inode, lista_path, lista_num):
		for val in lista_semb.curselection():
			lista_inode.insert(END, os.stat(os.path.abspath(lista_semb.get(val).replace('~/', ''))).st_ino) 
			lista_path.insert(END, lista_semb.get(val).replace('~/', ''))
			
		lista_num_dest, lista_num_src = listas_semb_ig()

		for i in range(0, len(lista_num_dest)):
			with open(lista_num_dest[i], 'r') as dest:
				dest_array = dest.read().split('\n')
			with open(lista_num_src[i], 'r') as src:
				src_array = src.read().split('\n')				
			lista_num.insert(END,len(filter(lambda x: x not in src_array, dest_array)))
				
	#listas para pasar por parametros 
	def listas_semb_ig(self, lista):
		lista_semb_act_dest = [lista.get(i) for i in lista.curselection()]
		lista_semb_act_src = []
		for key, value in dicc_fitx_semb.iteritems():
			for i in range(0, len(lista_semb_act_dest)):
				elem_x = dir_NameDst.get()+lista_semb_act_dest[i].replace('~', '')
				if elem_x in value:
					lista_semb_act_src.append(key)
					lista_semb_act_dest[i]=elem_x

		return lista_semb_act_dest, lista_semb_act_src

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
	def link(self, type):
		if not lista_ig.get(0,END):
			tkMessageBox.showwarning("Warning", "No hay ficheros iguales, la lista está vacía")
		else: 
			lista_ig_act_dest, lista_ig_act_src = listas_ig()
			esborra_link(lista_ig_act_dest)
			for i in range (0, len(lista_ig_act_dest)):
				if type == 'soft':
					os.symlink(dir_NameSrc.get()+'/'+lista_ig_act_src[i],lista_ig_act_dest[i])
				else:
					os.link(dir_NameSrc.get()+'/'+lista_ig_act_src[i],lista_ig_act_dest[i])

	def esborra_link(self, lista):
		if not lista and not list_ig.get(0,END):
			tkMessageBox.showwarning("Warning", "No hay ficheros en la lista")
		else: 
			for fitxer in lista:
				os.remove(fitxer)

	def esborra(self, lista):
		if not lista.get(0,END):
			tkMessageBox.showwarning("Warning", "No hay ficheros en la lista")
		else: 
			for fitxer in lista.get(0,END):
				fitxer=fitxer.replace('~',dir_NameDst.get()+'/')
				os.remove(fitxer)
			for elem_tupla in lista.curselection()[::-1]:
				lista.delete(elem_tupla)

	def renombra(self):
		if not lista_semb.get(0,END):
			tkMessageBox.showwarning("Warning", "No hay ficheros parecido, la lista está vacía")
		else: 
			print lista_semb.get(0,END)
			for a in lista_semb.curselection():
				b=lista_semb.get(a)
				b=b.replace('~', dir_NameDst.get()+'/')
				os.rename(b, b.replace('.txt','(copia).txt'))
			for a in lista_semb.curselection():	
				lista_semb.delete(a)
			print len(lista_semb.curselection())

	#Función crea GUI compara
	def compara_graf(self):
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

			llena_Listas(lista_inode, lista_path, lista_num)