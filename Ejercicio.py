#1 Guardar en memoria Ram las siguientes variable
#       -Entero 2000
#       -Flotante 19.9990
#       -String "Saludo"
#       -Lista con los numeros del 0 al 100, con salto 5
#       -Diccionario que almacene el nomvre completo de 3 amigos suyos
#       Con su respectivo numero de hijos
#  Escoja el nombre de la variable de la manera más descriptible posible
# Imprimalos en una sola linea y separados por coma

#2 Cree una lista con los numeros multiplos de 3, hasta el 100.
#  e imprimalos por pantalla
#  Invierta la lista creada en el último paso 
#  Elimine los 3 últimos elementos de la anterior lista
#  Cree una copia de la última lista, elimine el último valor
#  Y agregue su edad en esa misma posición.

#3 Cree un String con el siguiente parrafo:
"""
"""
#  Determine el numero de veces que se repite las vocales
#  Reemplace la palabra amor por hambre, y la palabra ojos por dientes
#  Coloque todas las letras en mayusculas
#  Revierta todo el texto 

###### Solución ######

#1-)
from Explicacion import Elemento


Entero=2000
Flotante=19.9990
Str="Saludo"
Lista=[i for i in range(0, 101, 5)]
diccionario={"Mariana Londoño":"5", "Luis Santacruz":"2", "Alejandro Ortega":"3"}
print(Entero)
print(Flotante)
print(Str)
print(Lista)
print(diccionario)

#2-)
Multipos=[i for i in range(0,100,3)]
print(Multipos)
Multipos