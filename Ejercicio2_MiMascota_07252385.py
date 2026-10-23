print("\nEjercicio 2: Mi Mascota en años humanos")
print("\nMi mascota")

nombre_mascota="Rocky"
tipo="perro"
edad_mascota="8"

#Regla popular: 1 año de perro equivale a 7 años humanos
edad_humana = edad_mascota * 7

#f-string: la f permite usar {Variables} dentro del texto
print(f"Mi{tipo} se llama {nombre_mascota}")
print(f"Tiene{edad_mascota} años de {tipo}")
print(f"¡En años humanos tendría {edad_humana} años!\n")