#Ejercicio 2
salario=float(input("Ingrese su salario: "))
descuento=0
salariofinal=0
if(salario<=900000):
  descuento=salario*0.15
elif(900000<salario<=2500000):
  descuento=salario*0.2
elif(2500000<salario):
  descuento=salario*0.25

salariofinal=salario-descuento
print("El salario final es: ",salariofinal)