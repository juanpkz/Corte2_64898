milista=[3,5,7,5]
b=[7,8,4,6,5]
opc = ''
while opc != 'salir': 

    opc = input('¿Que metodo desea utilizar?: ')

    if opc == 'borrar':
        dato = int(input('¿cual dato quiere borrar?: '))
        milista.remove(dato)
        print(milista)

    elif opc == 'agregar':
        dato = int(input('Ingrese un dato que desea que este al final: '))
        milista.append(dato)
        print(milista)
    
    elif opc == 'sacar':
       idx = int(input('Ingrese la posicion del numero que desea sacar: '))
       milista.pop(idx)
       print(milista)
    
    elif opc == 'limpiar':
       milista.clear()
       print(milista)
       
    elif opc == 'buscar':
        dato = int(input('¿Cual dato quiere buscar?: '))
        pos = milista.index(dato)
        print(f'El indice es {pos}')

    elif opc == 'comparar':
        print(f'El valor maximo de la lista es {max(milista)}')
        print(f'El valor minimo de la lista es {min(milista)}')

    elif opc == 'tamaño':
        print(len(milista))
    
    elif opc == 'contar':
        dato = int(input('¿Cual dato quiere contar : '))
        con = milista.count(dato)
        print(con)
    
    elif opc == 'sumar':
        res = sum(milista)
        print(f'El resultado de la suma de la lista es: {res}')
        
    elif opc == 'insertar':
        dato = int(input('¿Cual dato quiere insertar?: '))
        idx = int(input('Ingrese un indice: '))
        milista.insert(idx,dato)
    
    elif opc == 'confirmar':
        dato = int(input('¿Que datos desea confirmar: '))
        elm = dato in milista
        print(elm)

    elif opc == 'unir':
        milista.extend(b)
        print(milista)

    elif opc == 'ascender':
        milista.sort()
        print(milista)
    
    elif opc == 'invertir':
        milista.sort(reverse=True)
        print(milista)
        
    

   