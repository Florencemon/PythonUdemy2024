def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres = ['Juan', 'Karla', 'Guillermo']
desplegarNombres(nombres)
desplegarNombres('Carlos')
desplegarNombres((8, 9))
desplegarNombres([10, 11])

""""otra forma"""
def desplegarNombres(nombres):
    for nombre in nombres:
        print(nombre)

nombres=[]

while True:

    # Solicitar nombres al usuario y almacenarlos en una lista
    entrada = input("Introduce un nombre y S para SALIR: ")

    if entrada == "S":
        print("adios")
        print(nombres)
        break
    else:
        nombres.append(entrada)

    # Llamar a la función para desplegar los nombres
    desplegarNombres([nombres])
