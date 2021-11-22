#Ejercicio 1.py

año=int(input("Ingrese el año: "))
if (año%4==0):
  if(año%400==0):
    print("Es bisiesto")
  elif(año%100==0):
    print("No es bisiesto")
  else:
    print("Es bisiesto")
else:
  print("es un año común")