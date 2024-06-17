def factorial(numero):
    if numero <= 1:
        return 1
    else:
        return numero * factorial(numero-1)


resultado = factorial(int(input("diga un numero: ")))
print(f"el resultado es: ",resultado)