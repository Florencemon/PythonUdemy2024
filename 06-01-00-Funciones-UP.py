def suma(a, b):
    s = a + b
    return s


x = int(input("Ingrese el primer sumando: "))
y = int(input("Ingrese el segundo sumando: "))
z = suma(x, y)
print(f"{x} + {y} =", z)