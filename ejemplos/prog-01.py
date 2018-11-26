import sys
archivo = open(sys.argv[1], "r+")
contenido = archivo.read()
nombre = archivo.name
modo = archivo.mode
encoding = archivo.encoding
archivo.close()
print ("Estado del Archivo: " + ("Abierto", "Cerrado")[archivo.closed])
print ("Contenido")
print ("------------------------------------------------")
print (contenido)
print ("------------------------------------------------")
print ("Nombre del archivo: " + nombre)
print ("Modo de apertura :" + modo)
print ("Codificación: " + encoding)
