# i ,j ,k
import random as rand
def Matrices (filas,columnas):
    matriz = []
    for i in range (filas):
        matriz.append([])
        for j in range(columnas):

            num = rand.randint(1,10)
            #num = int(input(f'Ingrese el nuemero de la posicion [{i},{j}]: '))
            matriz[i].append(num)
    return matriz

def escalar(matriz,n):
    for i in matriz:
        for j in range(len(i)):
            i[j]= n *i[j]
    print(matriz)

def app():
    Filas = int(input('Ingrese el numero de filas: '))
    Columnas = int(input('Ingrese el numero de columnas: '))
    matriz = Matrices(Filas,Columnas)
    print(matriz)
    n = int(input('Ingrese un numero para escalar la matriz: '))
    escalar(matriz,n)




if __name__ == '__main__':
    app()