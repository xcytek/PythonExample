#!/usr/bin/env python
import time

class Materias:

	def __init__(self, clave, materia, semestre, profesor):
		self.clave = clave
		self.materia = materia
		self.semestre = semestre
		self.profesor = profesor
		print "--------------------"
		print "Materia registrada el ", time.asctime()
	
	def getData(self, clave):
		print "--------------------"
		print "\nClave: ", clave, "\nMateria: ", self.materia, "\nSemestre: ", self.semestre, "\nProfesor: ", self.profesor		