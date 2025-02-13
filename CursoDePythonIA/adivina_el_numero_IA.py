import random

print("🎯 Vamos a jugar a adivinar el número (entre 1 y 10)")

numero_adivinar = random.randint(1, 10)

while True:
    try:
        numero_usuario = int(input("Adivina el número: "))

        if numero_usuario < 1 or numero_usuario > 10:
            print("❌ Error: El número debe estar entre 1 y 10. Intenta de nuevo.")
            continue  # Vuelve a pedir un número válido

        if numero_usuario == numero_adivinar:
            print("🎉 ¡Has acertado! 🎉")
            break  # Sale del bucle al adivinar
        else:
            print("❌ Has fallado. Intenta de nuevo.")

    except ValueError:
        print("❌ Error: Introduce un número válido.")
