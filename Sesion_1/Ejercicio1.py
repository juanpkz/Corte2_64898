n = input('Ingrese un numero: ')

dimension = len(n)
contador = 0
if 2< dimension < 8:

    for i in n:
        if i == '5':
            print('Salto')
            contador += 1
        else:
            print(i)
            
    print(f'Numeros iguales a 5: {contador}')
    print(f'Numeros diferentes de 5: {dimension-contador}')
    print(f'Total de digitos: {dimension}')     
else:
    print('fuera de rango')
