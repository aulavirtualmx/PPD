import sys
archivo = open(sys.argv[1], "r+")
nombre = archivo.name
modo = archivo.mode
encoding = archivo.encoding
print ("Estado del Archivo: " + ("Abierto", "Cerrado")[archivo.closed])
print ("Contenido")
print ("------------------------------------------------")
lineas = archivo.readlines()
for i in range(len(lineas)):
  print(lineas[i], end="")
print ("------------------------------------------------")
print ("Nombre del archivo: " + nombre)
print ("Modo de apertura :" + modo)
print ("Codificación: " + encoding)
archivo.close()
