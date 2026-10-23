print("\n^+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("Ejercicio 9: Tienda de Mascota Interactiva")
print("TIENDA DE MASCOTAS DE GRECIA GUTIERREZ")
#input() le ´regubta al usuario y guarda lo que escribr en la varible
#input () SIRMPRE guarda TEXTO, aunque escribas un número
mascota = input("\n¿Qué mascota quieres adoptar?")
#Si el usuario escribe hamster, ahora mascota vale "hamster"

#float() convierte el texto a número con decimales para poder hacer cuentas
precio_mascota = float(input("¿Cuánto cuesta el/la {hamster}? $"))
#Si el ususario escribe 1500, ahora precio_mascota vale 1500.0
precio_alimento = float(input("¿Cuanto cuesta el mes del alimento?"))
#Si el usuario escribe 300, ahora precio_alimento vale 300
#int() convierte el texto a número entero, porque los meses no llevan decimales
meses = int(input("¿Para cuántos meses quieres alimento?"))
#Si el usuario escribe 3, ahora meses vale 3

#Calculamos cuánto gasto en alimento, esta formula dice: costo_alimentos = 350.0 * 3
costo_alimentos = precio_alimento * meses
#Ahora costo_alimento vale 1050.0

#Calculamos el total, esta formula dice: total = 1500.0 + 1050.0
total = precio_mascota + costo_alimentos
#Ahora total vale  2550.0

print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Ticket de compra")
#El :.2f muestra 2 decimales, como se ve el dinero
print(f"Macota: {mascota}  ${precio_mascota:.2f}")
print(f"Croquetas por {meses} meses: ${costo_alimentos:.2f}")
print(f"\nTOTAL A PAGAR: ${total:.2f}\n")
print("\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")