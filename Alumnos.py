#!/usr/bin/env python
import time

class Alumnos:
	
	def __init__(self, paterno, materno, nombre, matricula):
		self.paterno = paterno
		self.materno = materno
		self.nombre = nombre
		self.matricula = matricula		
		print self.paterno, " ", self.materno, " ", self.nombre, " ha sido registrado el ",time.asctime()
		
		
	def inscribirMateria(self, matricula):
		print "--------------------"
		print "Inscrito!"
		
		
	def getData(self, matricula):
		print "--------------------"
		print "\nMatricula: ", matricula, "\nAp. Paterno: ", self.paterno, "\nAp. Materno: ", self.materno, "\nNombre: ", self.nombre
		raw_input()