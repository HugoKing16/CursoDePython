
texto = "Bienvenido al test sobre el queso"
print("\n" + texto + "\n" + "-" * len(texto) + "\n")

puntuacion = 0

opcion = input("Pregunta 1: ¿Que haces cuando ves una tabla de quesos?\n"
                "A - Sales corriendo\n"
                "B - Pruebo un o dos quesos\n"
                "C - Me como la tabla entera\n")

if opcion == "A":
    puntuacion += 0 
    
elif opcion == "B":
    puntuacion += 5    
elif opcion == "C":
    puntuacion += 10
else:
    print("Opción posble es A, B o C")
    exit()            


opcion = input("Pregunta 2: ¿Te gusta la hamburguesa con queso?\n"
                "A - Sin queso\n"
                "B - Con queso\n"
                "C - Pan y  queso\n")

if opcion == "A":
    puntuacion += 0 
    
elif opcion == "B":
    puntuacion += 5    
elif opcion == "C":
    puntuacion += 10
else:
    print("Opción posble es A, B o C")
    exit()      
    
opcion = input("Pregunta 3: ¿Eres intolerante a la lactosa?\n"
                "A - Si\n"
                "B - A veces\n"
                "C - No\n")      

if opcion == "A":
    puntuacion += 0 
    
elif opcion == "B":
    puntuacion += 5    
elif opcion == "C":
    puntuacion += 10
else:
    print("Opción posble es A, B o C")
    exit()      



print(puntuacion)

