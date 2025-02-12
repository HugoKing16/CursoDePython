import random


print("Vamos a jugar adivinar el numero")


numero_adivinar = random.randint(1, 10)
numero_usuario = int(input("Adivina el numero: "))

if numero_usuario > 10:
    print("Te has pasado era entre 1 y 10")
    
if numero_usuario < 1:
    print("Te has quedado corto era entre 1 y 10")
    
    

if numero_adivinar == numero_usuario:
    print("Has acertado!")
else:
    print("Has fallado!")
    print("El numero correcto era: {}".format(numero_adivinar))
    
