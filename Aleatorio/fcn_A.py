
import random as r

def es_par(numero): 
     return numero % 2 == 0

def Aleatorio():
    
        lista = 0
        orden = "par"

        while lista < 10:
            numero = r.randint(100, 120)

            if numero == 110 or numero == 115 or numero == 119:
                continue

            elif orden == "par" and es_par(numero):
                lista += 1
                orden = "no es par"
                print(numero)

            elif orden == "no es par" and not es_par(numero):
                lista += 1
                orden = "par"
                print(numero)
