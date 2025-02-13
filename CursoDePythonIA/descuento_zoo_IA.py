
def obtener_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("❌ Error: Introduce un número válido.")

def obtener_tipo_carnet():
    while True:
        tipo = input("📜 Dime tu tipo de carnet (E: Estudiante / P: Pensionista / F: Familia numerosa / N: Nada): ").strip().upper()
        if tipo in ["E", "P", "F", "N"]:
            return tipo
        print("❌ Error: Introduce una opción válida (E, P, F o N).")

# Pedimos los datos al usuario con validación
edad = obtener_entero("🎂 Dime tu edad: ")
tipo_de_carnet = obtener_tipo_carnet()

# Condición de descuento
if (25 <= edad <= 35 and tipo_de_carnet == "E") or \
   edad <= 10 or \
   (edad >= 65 and tipo_de_carnet == "P") or \
   tipo_de_carnet == "F":
    print("✅ ¡Se te aplica el descuento!")
else:
    print("❌ No se te aplica el descuento.")

