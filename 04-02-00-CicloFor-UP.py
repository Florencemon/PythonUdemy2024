nombres=["carla","yolanda","maria","pedropedropedro","daniel"]
nombres[2]="ivonne"


for nombre in nombres:
    print(nombre)
else:print("***FIN***")

print(len(nombres))

nombres.append("lorenzo")
print(nombres[-1])

nombres.insert(1,"octavio")
print(nombres)
nombres.pop(2)
print(nombres)
del nombres[0]
print(nombres)
nombres.clear()
print(nombres)
del nombres
print(nombres)