cadena = "Hola Mundo!"
print(cadena[6])
print(len(cadena))
texto=''

#accediendo con un for

for i in cadena:
    texto += str(f'{i},')
    print(texto)

#accediendo con un while
contador = 0
texto2=''

while contador < len(cadena):
    texto2 += str(f'{cadena[contador]},')
    contador += 1
print(texto2)