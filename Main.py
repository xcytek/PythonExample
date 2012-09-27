#!/usr/bin/env python
import Alumnos
import Materias
import Archivos

n = "s"
archivo = Archivos.Archivos()

while n == "s":

   	print "-------------------------- SISTEMA DE REGISTRO ESCOLAR -------------------------\n"
	print "Menu Principal:\n1) Alumnos\n2) Materias\n3) Crear Nuevo Archivo\n4) Salir\n"
	opcion = int(raw_input("-> "))
	
	if opcion == 4:
		n = "n"
		
	elif opcion == 1:
		print "\nMenu Alumnos:\n1) Registrar\n2) Obtener Datos\n3) Longitud de Objeto\n4) Salir"
		opc_alumno = int(raw_input("-> "))
		
		if opc_alumno == 4:
			n = "n"
			
		elif opc_alumno == 1:	
			paterno = raw_input("Apellido Paterno: -> ")
			materno = raw_input("Apellido Materno: -> ")
			nombre = raw_input("Nombre(s): -> ")
			matricula = raw_input("Matricula: -> ")
			
			parametro_archivo = "\n---------------------------\n#Alumno\n", matricula, "\n", paterno, "\n", materno, "\n", nombre
			
			try:
				archivo.addLineas("Alumnos.dat",parametro_archivo)
				alumno = Alumnos.Alumnos(paterno, materno, nombre, matricula)					
			except:
				print "Error. No se puede registrar el nuevo alumno!..."
			
			
		elif opc_alumno == 2:
			matricula = raw_input("Matricula: -> ")
			alumno.getData(matricula)
			
		elif opc_alumno == 3:
			long = alumno.len(alumno)
			print long
			
	elif opcion == 2:
		print "Menu Materias:\n1) Registrar\n2) Obtener Datos\n3) Salir"
		opc_materia = int(raw_input("-> ")) 
		
		if opc_materia == 3:
			n = "n"
		
		elif opc_materia == 1:	
			clave = raw_input("Clave: -> ")
			nombre_materia = raw_input("Materia: -> ")
			semestre = raw_input("semestre: -> ")
			profesor = raw_input("Profesor: -> ")
			parametro_archivo = "\n---------------------------\n#Materia\n", clave, "\n", nombre_materia, "\n", semestre, "\n", profesor
			try:
				archivo.addLineas("Materias.dat",parametro_archivo)
				materia = Materias.Materias(clave, nombre_materia, semestre, profesor)
			except:
				print "Error. No se puede registrar el nuevo alumno!..."
			
		
		elif opc_materia == 2:	
			clave = raw_input("Clave: -> ")
			materia.getData(clave)


raw_input("Version de Prueba 1.0. Desarrollado en La Ruta del Vino, Mexico")

