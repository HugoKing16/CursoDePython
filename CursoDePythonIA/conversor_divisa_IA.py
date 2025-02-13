
def obtener_numero(mensaje):
    while True:
        try:
            return float(input(mensaje))
        except ValueError:
            print("❌ Error: Introduce un número válido.")

# Pedir datos al usuario con validación
cantidad_de_libras = obtener_numero("💷 Introduzca la cantidad en libras: ")
conversion_libra_euro = obtener_numero("💱 Introduzca la tasa de conversión de libra a euro: ")

# Realizar conversión
cantidad_en_euros = cantidad_de_libras * conversion_libra_euro

# Mostrar resultado con 2 decimales
print(f"💶 La cantidad equivalente en euros es: {cantidad_en_euros:.2f}€")
