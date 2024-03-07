lista = []

num = int(input("Ingrese un numero: "))
for i in range(num):
    lista.append(
        int(input("Ingrese"))
    )
    print(lista)

def Eliminar_duplicados(lista1):

   for num in lista1:
         lista1.remove(9)
         return lista1

lista1 = [1,3,9,9,10]
print("se elimino el duplicado",Eliminar_duplicados(lista1))

def sumar(lista):
    return sum(lista)

lista = [1,2,3]
print(sumar(lista))


def comparacion(lista1,lista2):
      for num in lista1:
          if num in lista2:
           return True
          return False

lista1 = [1,2,3]
lista2 = [8,5,2]
print(comparacion(lista1, lista2))



