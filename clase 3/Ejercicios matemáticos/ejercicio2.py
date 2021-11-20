print("Aplicativo de millas-kilómetros")
print(" "*12 + "1. Millas a Km")
print(" "*12 + "2. Km a millas")
opcion=input("Elija la opción: ")
L=float(input("Ingrese la longitud: "))
#Elección de la opción
if (opcion=="1"):
    print(" "*12 + "1. Millas a Km")
    print(L, "millas", "son", L*1.61, "kilómetros")
elif (opcion=="2"):
    print(" "*12 + "2. Km a Millas")
    print(L, "Km", "son", round(L/1.61, 3 ), "millas")

