import math as m


operacion = input('Seleccione la operacion que desea realizar\n a).seno\n b).cos\n c).tangente\n d).exponencial\n e).logaritmo natural\n')
numero = eval(input('Ingrese el numero con el cual desea hacer la operacion: '))

def pasar_grados_a_radianes(grados): 
    return grados * m.pi / 180
def Calculadora():

    if operacion == 'seno' or operacion == 'a':
        tipo = int(input("El numero que quiere ingresar esta en\n1.grados \n2.radianes\n"))
        if tipo == 1:
            tipo_de_numero = pasar_grados_a_radianes(numero) 
        elif tipo == 2:
            tipo_de_numero = numero
        resultado= round(m.sin(tipo_de_numero),3)
        print(f'El resultador del seno de {numero}\n es {resultado}')

    elif operacion == 'coseno'or operacion == 'b':
        tipo = int(input("El numero que quiere ingresar esta en\n1.grados \n2.radianes"))
        if tipo == 1:
            tipo_de_numero = pasar_grados_a_radianes(numero)
        elif tipo == 2:
            tipo_de_numero = numero
        resultado= round(m.cos(tipo_de_numero),3)
        print(f'El resultador del coseno de {numero}\n es {resultado}')

    elif operacion == 'tangente'or operacion == 'c':
        tipo = int(input("El numero que quiere ingresar esta en\n1.grados \n2.radianes"))
        if tipo == 1:
            tipo_de_numero = pasar_grados_a_radianes(numero)
        elif tipo == 2:
            tipo_de_numero = numero
        resultado= round(m.tan(tipo_de_numero),3)
        print(f'El resultador de la tangente de {numero}\n es {resultado}')

    elif operacion == 'exponencial'or operacion == 'd':
        resultado= round(m.exp(numero),3)
        print(f'El resultador exponencial de {numero}\n es {resultado}')

    elif operacion == 'logaritmo natural'or operacion == 'e':
        resultado= round(m.log(numero),3)
        print(f'El resultador del logaritmo natural de {numero}\n es {resultado}')