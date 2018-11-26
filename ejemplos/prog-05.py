import sys
archivo = open ("datos.txt","a")
archivo.write(sys.argv[1]+ "\n")
archivo.close()
