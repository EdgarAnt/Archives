#Protocolo
#practica02
archivo = open("Mi_Cancion_Favorita.txt", "r")

for line in archivo:
    print(line, end="\b")
archivo.close()
