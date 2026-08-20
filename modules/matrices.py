import numpy as np

def calcular_determinante(): 
    print("\n--- 🧮 Cálculo de Determinante (Matriz 2x2) ---")

#El determinante es el número que te dice cuánto se ha multiplicado el tamaño original de esa área.
#Los determinantes y las inversas SOLO se pueden hacer en matrices cuadradas (2x2, 3x3, etc etc)



# Si el determinante es 0: El área desaparece y se vuelve cero. 
#  si una matriz tiene determinante 0, significa que está "rota" y no se puede invertir; no tiene salida).

tamano = int(input("¿De qué tamaño es la matriz? (Escribe 2 o 3): "))


if tamano == 2:
        print("Has elegido una matriz de 2x2.")
        # (Aquí pondremos el código para pedir los 4 números de la 2x2 en el siguiente paso)
        
        
elif tamano == 3:
        print("Has elegido una smatriz de 3x3.")
        # (Aquí pondremos el código para pedir los 9 números de la 3x3 en el siguiente paso)
        

else:
        print("¡Error! Solo sé calcular matrices de orden 2 o 3 por ahora.")



   