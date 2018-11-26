kimport sys
archivo = open(sys.argv[1], "r+")
nombre = archivo.name
modo = archivo.mode
encoding = archivo.encoding
print ("Estado del Archivo: " + ("Abierto", "Cerrado")[archivo.closed])
print ("Contenido")
print ("------------------------------------------------")
linea = archivo.readline()
while linea:
  print(linea,end="")
  linea = archivo.readline()
print ("------------------------------------------------")
print ("Nombre del archivo: " + nombre)
print ("Modo de apertura :" + modo)
print ("Codificación: " + encoding)
archivo.close()
