#Tipos de datos

#Boolean
boolean1=True
boolean2=False

if (boolean1):
    print('Usuario "Elver Galarga" ')

# Enteros, flotante
a=1
b=2.5
print(a,b)

#Listas 

A=[1, 2, 3, 4, 5, 6, 7]
print(A)
Elemento=A[2]
print(Elemento)
slice = A[3:5]
print("Rebanada = ", slice)

B=["a", "z", "c", "k", "l", "u"]
print("Listado string's: " ,B)
print("Impresión del 3ro al ultimo elemento del listado: ", B[2:7])
print("Impresión del 3ro al ultimo elemento del listado: ", B[2:]) #Se deja indicado los 2 puntos para que tome el ultimo tomandolo
print("Impresión del 1ro al ultimo elemento del listado de 2 en dos: ", B[0:-1:2])
B.append(1000)
print(B)
B.pop(0)
print(B)
print(B.count("a")) #Contar cuantas veces está lo que está dentro del parentesis
# B.reverse() #Pone la lista de derecha a izquierda pero dañando la lista original
lista=[i for i in range(2,100,3)]
lista2=lista.copy()
lista2.reverse()
print("La lista original: ", lista)
print("La lista al revés es: " , lista2)

##Strings
str1= "Hola curso de informatica"
str2= str1.replace("a", "x")
print(str2)

##Diccionarios
diccionario={"Car":"Carro", "House":"Casa"}
print(diccionario["House"])
