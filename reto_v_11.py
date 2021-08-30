#Ejercicio 1:
#• Crea un programa que pida dos números por teclado. El programa tendrá una función 
#llamada “DevuelveMax” encargada de devolver el número más alto de los dos
#introducidos.
print("Calcular número mayor")
valor1=int(input("ingrese el primer valor: "))
valor2=int(input("ingrese el segundo valor: "))


def DevuelveMax(valor1, valor2):
    if valor1>valor2:
        print(str(valor1) + " Es mayor")
    else:
        print(str(valor2) + " Es mayor")    

DevuelveMax(valor1, valor2)

#Ejercicio 2:
#• Crea un programa que pida por teclado “Nombre”, “Dirección” y “Tfno”. Esos tres datos 
#deberán ser almacenados en una lista y mostrar en consola el mensaje: “Los datos 
#personales son: nombre apellido teléfono” (Se mostrarán los datos introducidos por 
#teclado).

print("Hola, porfavor ingresa tus datos personales a continuacion")

nombre=str(input("Ingresa tu nombre: "))
direccion=str(input("Ingresa tu direcion"))
telefono=str(input("Ingresa tu número de teléfono"))

datos_personales=[
    nombre,
    direccion,
    telefono
]
print("tus datos personales son: ")
print(datos_personales)
      
#Ejercicio 3:
#• Crea un programa que pida tres números por teclado. El programa imprime en consola 
#la media aritmética de los números introducidos.

print("Ingresa 3 números para obtener su media aritmética")

numero1=int(input("Ingresa el primer número"))
numero2=int(input("Ingresa el segundo número"))
numero3=int(input("Ingresa el tercer número"))

lista_numeros=[numero1, numero2, numero3]

def mean(lista):
    suma= 0
    for x in range(len(lista)):
        suma=suma+lista[x]
    cantidad_valores_lista = len(lista)
    media_aritmetica = suma/cantidad_valores_lista

    return media_aritmetica

print(mean(lista_numeros))
