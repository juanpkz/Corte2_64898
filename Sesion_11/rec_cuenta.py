def imprimir(x):
    if x >0 :
        imprimir(x-1)
        print(x)
    else :
        print (f'Finalizo{x}')


if __name__ == '__main__':
    imprimir(5)