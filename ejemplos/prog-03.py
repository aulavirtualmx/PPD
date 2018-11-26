import sys
archivo = open(sys.argv[1], "r+")
nombre = archivo.name
modo = archivo.mode
encoding = archivo.encoding
print ("Estado del Archivo: " + ("Abierto", "Cerrado")[archivo.closed])
print ("Contenido")
print ("------------------------------------------------")
for linea in archivo:
  linea = linea[:-1]
  print(linea)
print ("------------------------------------------------")
print ("Nombre del archivo: " + nombre)
print ("Modo de apertura :" + modo)
print ("Codificación: " + encoding)
archivo.close()
