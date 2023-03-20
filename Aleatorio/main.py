from fcn_A import Aleatorio


def main():
    
    print("Los numeros aletorios son los siguientes: ")
    Aleatorio()

    print("Desea imprimir nuevos numeros?: ")

    opc = input('si o no: ')

    if opc == 'si':
       Aleatorio()

    elif opc == 'no':
      print("Fin del programa")


if __name__ == "__main__":
    main()