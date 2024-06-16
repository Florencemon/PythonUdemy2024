print("proporcione los sig. datos:")
titulo=input("proporcione el nombre del libro: ")
id=int(input("proporcione el ID del libro: "))
precio=float(input("proporcione el precio del libro: "))
envioGratis=input("el envio es gratuito?: True/False")

enviogatuito="Envio pago"
if envioGratis.lower == "True":
    enviogatuito="Envio gratis"



print(f"Detalles: \nnombre del libro: {titulo}\nID del libro: {id}\nprecio del libro: {precio}\nPrecio del envio: {enviogatuito}")
