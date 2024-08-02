texto = input('Ingrese aquí su texto: ')
letras = []
texto = texto.lower()
letras.append(input('Ingresa tu primera letra de elección: '))
letras.append(input('Ingresa tu segunda letra de elección: '))
letras.append(input('Ingresa tu tercera letra de elección: '))

print(f"El texto contiene la letra {letras[0]} {texto.count(letras[0])} veces")
print(f"El texto contiene la letra {letras[1]} {texto.count(letras[1])} veces")
print(f"El texto contiene la letra {letras[2]} {texto.count(letras[2])} veces")

palabras = texto.split()
print(f"El texto contiene {len(palabras)} palabras")


palabras.reverse()
texto_invertido = " ".join(palabras)
print(f"Si el texto estuviera invertido quedaría de la sigueinte forma: {texto_invertido}")

print(f"La primera letra del texto es: {texto[0]}")
print(f"La última letra del texto es: {texto[-1]}")


buscar_python = 'python' in texto
dic = {True: "sí", False:"no"}
print(f"La palabra Python {dic[buscar_python]} aparece en el texto")