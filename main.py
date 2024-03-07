# This is a sample Python script.

# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

#suma de elementos
def suma_elementos(arreglo):
    suma= 0
    for num in arreglo:
        suma += num
    return suma

arreglo = [1,2,3,4,5]
print("Esta es la suma", suma_elementos(arreglo))

#ordenamiento de burbuja
def ordenamiento(arreglo1):
    num1 = len(arreglo1)

    for i in range(num1 - 1):
        for j in range(num1 -1-i):
            if arreglo1[j] > arreglo1[j + 1]:
                 arreglo1[j], arreglo1[j + 1] = arreglo1[j + 1], arreglo1[j]

elementos = [8,3,1,10,7]
ordenamiento(elementos)
print("Este es el ordenamiento", elementos)

def encontrar_maximo(arreglo2):
    maximo = arreglo2[0]
    for num2 in arreglo2:
        if num2 > maximo:
            maximo = num2
            return maximo

arreglo2 = [10,2,50,4,5]
print("Aca buscamos el maximo", encontrar_maximo(arreglo2))

#fibonacci
def fibonacci(n):

   if n> 1:
       return fibonacci(n-1) + fibonacci(n-2)
   return n

for i in range(10):
    print("este es fibonacci", fibonacci(i))

#ordenamiento por seleccion

def ordenamientoporselescion(arreglo):

    tamano = len(arreglo)
    for i in range(tamano):
        min=i
        for j in range(i+1,tamano):
            if arreglo[min] > arreglo[j]:
                min=j
        aux=arreglo[i]
        arreglo[i]=arreglo[min]
        arreglo[min]=aux
    return arreglo

arreglo=[4,6,3,8,10,1,2,0,9,7,5]
print("Este es mi arreglo ordenado seleccion", ordenamientoporselescion(arreglo))

def buscar(arreglo,objetivo):

    for num in arreglo:
        if num == objetivo:
            return True
    return False


arreglo=[4,6,3,7,9]
numero_objetivo= 3
print("el numero ",numero_objetivo,"esta presente en el arreglo",buscar(arreglo,numero_objetivo))


def eliminiar(arreglo):

    for num in arreglo:
        if num == num:
            arreglo.remove(num)
            return arreglo
arreglo=[4,4,3,1,9,1,2,0]
print("Se eliminaron los numeros duplicados del arreglo:",eliminiar(arreglo))

def sub(subcadena):


      if subcadena in cadena:
       return subcadena

cadena = "Estructura Datos"
subcadena = "Datos"
print(sub(subcadena))

def invertir(arreglo):

    arreglo.reverse()
    return arreglo
arreglo=[1,2,3,4,5,6,7,8,9]
print("Se invirtio",invertir(arreglo))

def ocurrencia(arreglo):

    for num in arreglo:

      return arreglo

arreglo=[{"yoan":"27"},{"lola":"22"},{"juan":"19"}]
print(ocurrencia(arreglo[1]))





