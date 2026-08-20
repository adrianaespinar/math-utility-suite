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

        a1 = int(input("Indica el número de la fila 1 columna 1: "))
        a2 = int(input("Indica el número de la fila 1 columna 2: "))
        a3 = int(input("Indica el número de la fila 2 columna 1: "))
        a4 = int(input("Indica el número de la fila 2 columna 2: "))

        # Se puede poner en bloque o en una línea:
        matriz = np.array([[a1, a2], [a3, a4]])

        determinante = np.linalg.det(matriz)

        return round(determinante, 2)

    elif tamano == 3:
        print("Has elegido una smatriz de 3x3.")
        
        a1 = int(input("Fila 1, Columna 1: "))
        a2 = int(input("Fila 1, Columna 2: "))
        a3 = int(input("Fila 1, Columna 3: "))
        a4 = int(input("Fila 2, Columna 1: "))
        a5 = int(input("Fila 2, Columna 2: "))
        a6 = int(input("Fila 2, Columna 3: "))
        a7 = int(input("Fila 3, Columna 1: "))
        a8 = int(input("Fila 3, Columna 2: "))
        a9 = int(input("Fila 3, Columna 3: "))

        
        matriz = np.array([
            [a1, a2, a3],
            [a4, a5, a6],
            [a7, a8, a9]
        ])

        
        determinante = np.linalg.det(matriz)

        return round(determinante, 2)
        

    else:
        print("¡Error! Solo sé calcular matrices de orden 2 o 3 por ahora.")



   # Hello there!
   #Prueba2s