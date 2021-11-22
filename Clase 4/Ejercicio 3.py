#Ejercicio 3.py
#Realice un programa, que determine el número mayor para una cantidad indeterminada
# de numeros (para ello utilice el ciclo while)
a=0
lista=[]
print("Si quiere detener el ciclo, digite el valor de -1")
while a!=-1:
  a=float(input("Ingrese un número: "))
  lista.append(a)
Numero_mayor=max(lista)
print("El numero mayor es: ",Numero_mayor)