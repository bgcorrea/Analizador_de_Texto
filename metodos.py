texto = "Este es el texto de Federico"

resultado = texto.lower()
print (resultado)

resultado = texto.upper()
print (resultado)

resultado = texto.capitalize()
print (resultado)

resultado = texto.split("t")
print (resultado)

a = "Aprender"
b = 'Python'
c = 'es'
d = 'genial'
e = '_'.join([a, b, c, d])
print(e)

resultado = texto.find("t") # Si no encuentra lo que buscas dara -1
print (resultado)

resultado = texto.replace("Federico", "Juan")
print (resultado)



