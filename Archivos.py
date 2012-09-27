#!/usr/bin/env python
import time
 
class Archivos:
 
	def crearArchivo(self, nombre):
		nom_archivo = raw_input("Nombre del Archivo: -> ")
		nom_archivo = nom_archivo + ".dat"
		f = open(nom_archivo,"w")
		print "Archivo creado!... ",nom_archivo
		
	
	def leerArchivo(self, nom_archivo):
		f = open(nom_archivo,"r")
		print f
		
	
	def addLineas(self, nom_archivo, parametro):
		f = open(nom_archivo,"a")	
		f.writelines(parametro)
		
