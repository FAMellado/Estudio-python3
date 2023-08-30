# comentarios con un simple #
## al parecer python no soporta multi-line comments

print("Wena que ocurre realmente")

# print con parentesis y "" o ''e

# Variables

name = "Felipe"
age = 24


#Tuplas
punto=(3,4,5,6,7)
a,b,c,d,e = punto
#aparentemente tienen que encajar con el numero de tuplas para poder ser guardadas correctamente en variables con esta forma
## Las tuplas son SIEMPRE IMMUTABLES, no pueden ser alteradas despues de ser creadas

print(a,b,c,d,e)


#If/Else

if age >= 24:
    print ("Otro año de mierda")
else:
    print ("Sufrimiento")

frutitas = ["manzana", "poroto" , "huevito" , "king"]


# Ciclo For
for xd in frutitas:
    print(xd)


# Ciclo While

cuenta = 0
while cuenta < 5:
    print(cuenta)
    cuenta += 1

# += para ir sumando 
# =+1 seria lo mismo que "cuenta = 1", no suma a la variable sino que solo la asigna entonces el loop se queda pegado y se va a la ctm

# Funciones

def saludar(nombre):
    print(f"Hola, {nombre}! Eres muy weta")

saludar("Felipe")


#Estructuras

#Listas / Arreglos
numeros = ["uno", "dos", "tres" ,"veinte"]
print(numeros[3])


#Diccionarios
# Colecciones de PARES "llave-valor" 

persona={"nombre": "Felipe", "Habilidad": "Autismo"}
print(persona["nombre"])
print(persona["Habilidad"])

# SETS - Lista DESORDENADA de elementos unicos, utiles para tareas como remover duplicados de una lista

colores = {"rojo", "blanco", "azul"}

#Arrays | Python no tiene arrays incorporados pero se puede importar el modulo array para crear un arreglo de un tipo de dato especifico

from array import array 
number = array('i', [1,2,3,4,5]) # 'i' representa integer type



