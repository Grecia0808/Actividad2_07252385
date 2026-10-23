print("\n===================================================================")
print("Ejercicio 6: Vidas y daño")
print("===========================BATALLA====================")
#Damos de alta la variable personaje y vida
personaje = "Zavitar"
vida = 100
class Zavitar:
    ...

print(f"\nMi personaje se llama {personaje} y empieza con {vida} de vida")
#Como vida vale 100, esta formulada dice = 100 -25
vida = vida - 25
print(f"Me dio un golpe de FlashReverso, ahora tengo vida: {vida}")
#Ahora vida vale 75, esta formula dice: vida = 75 - 40
print(f"Ah, ahora me toco el golpe de Snart, tengo vida: {vida}")
#Ahora vida vale 35, esta formula dice = 35 - 15
vida = vida - 15
print(f"Me toco una flecha verde enemiga!, tengo de vida: {vida}")
#Ahora vida vale 20, esta formula dice: vida = 20 + 30
vida = vida + 30
print(f"Tomó una poción... mi vida: {vida}")

print(f"\n{personaje} terminó la batalla con {vida} HP\n")
print("=====================================================================")
