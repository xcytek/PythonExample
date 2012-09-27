nom_archivo = raw_input("Nombre del Archivo: -> ")
nom_archivo = nom_archivo + ".dat"
f = open(nom_archivo,"w")
print "Archivo creado!... ",nom_archivo

i = 0
while i < 100:
	i += 1
	f.writelines(str(i)+"\n")
	raw_input()