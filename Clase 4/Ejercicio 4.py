#Ejercicio 4
numero=1
lista1=[]
lista2=[]
while (numero!=0):
  numero=float(input("Digite un número para la secuencia, si quiere parar escriba 0: "))
  if numero%2!=0:
    lista1.append(numero)
  elif numero%2==0:
    lista2.append(numero)
Numerosimpares=len(lista1)
Numerospares=len(lista2)-1
print("La cantidad de números pares digitados son: ",Numerospares,"Y la cantidad de numeros impares digitados son: ",Numerosimpares)