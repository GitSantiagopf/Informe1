#Ejercicio 5
numerosecreto=24
n=int(input("Ingrese un número: "))
while n!=numerosecreto:
  print("¡Ja, Ja! ¡Estás atrapado en mi ciclo!")
  n=int(input("Ingrese otro número: "))
  if (n==numerosecreto):
    print("¡Bien hecho muggle! Eres libre ahora")