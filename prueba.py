#CALCULADORA

def suma (a,b):
    z= a+b
    return z

def resta (a,b):
    z= a-b
    return z


def multiplicacion (a,b):
    z= a*b
    return z

def division (a,b):
    z= a/b
    return z


a=int(input("diga un numero: "))
b=int(input("diga otro numero: "))

calculo=int(input("que operación desea realizar? Seleccione un numero:\n1.Suma\n2.Resta\n3.Multiplicación\n4.División\n"))
print(f"Opcion elegida: {calculo}")
if calculo ==1:
    resultado =suma(a,b)
elif calculo==2:
    resultado =resta(a,b)
elif calculo==3:
    resultado =multiplicacion(a,b)
elif calculo==4:
    if b==0:
        b=int(input("no se puede dividir por 0, ingrese nuevamente un numero distinto de 0:"))
        resultado =division(a,b)
else: print("Opción inválida")


print(f"el resultado es {resultado}")

