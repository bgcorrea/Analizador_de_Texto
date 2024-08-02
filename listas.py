mi_lista = ['a','b','c']
mi_lista2 = ['d','e','f']

print(type(mi_lista))
resultado = len(mi_lista)
print(resultado)
resultado = mi_lista[0:2] # Al 2 no lo incluye
print(resultado)
print(type(mi_lista + mi_lista2))

mi_lista3 = mi_lista + mi_lista2
print(mi_lista3)

mi_lista3.append('g') # Se agrega al final
print(mi_lista3)

mi_lista3.pop(4) # Pop elimina el indice que le indiquemos
print(mi_lista3)

lista = ['g', 'o', 'b', 'm', 'c']
lista.sort()
print(lista)

lista.reverse()
print(lista)