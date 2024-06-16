print("Proporcione los siguientes datos:")
titulo = input("Nombre del libro: ")
id = int(input("ID del libro: "))
precio = float(input("Precio del libro: "))
envioGratis = input("¿El envío es gratuito? (True/False): ")

enviogatuito = "Envío pago"  # Por defecto, el envío se asume como pago

# Convertimos la entrada de envioGratis a booleano correctamente
if envioGratis.lower() == "true":
    enviogatuito = "Envío gratis"

print(f"Detalles:\nNombre del libro: {titulo}\nID del libro: {id}\nPrecio del libro: {precio}\nY el envío es: {enviogatuito}")
