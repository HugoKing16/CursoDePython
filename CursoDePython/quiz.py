
texto = "Bienvenido al test sobre el queso"
print("\n" + texto + "\n" + "-" * len(texto) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: Que haces cuando ves una tabla de quesos?\n"
                "A -Sales corriendo\n"
                "B - Pruebo un o dos quesos\n"
                "C - Me como la tabla entera\n")

if opcion == "A":
    puntuacion = puntuacion + 0   
    
if opcion == "B":
    puntuacion = puntuacion + 5
    
if opcion == "C":
    puntuacion = puntuacion + 10            