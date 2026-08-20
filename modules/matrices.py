import numpy as np

def calcular_determinante(): 
    print("\n--- 🧮 Cálculo de Determinante (Matriz 2x2) ---")

#El determinante es el número que te dice cuánto se ha multiplicado el tamaño original de esa área.
#Los determinantes y las inversas SOLO se pueden hacer en matrices cuadradas (2x2, 3x3, etc etc)



# Si el determinante es 0: El área desaparece y se vuelve cero. 
#  si una matriz tiene determinante 0, significa que está "rota" y no se puede invertir; no tiene salida).

tamano = int(input("¿De qué tamaño es la matriz? (Escribe 2 o 3): "))

    # Pedimos los números uno a uno usando input() y los convertimos a entero con int()
    a = int(input("Introduce el valor de la posición [fila 1, columna 1]: "))
    b = int(input("Introduce el valor de la posición [fila 1, columna 2]: "))
    c = int(input("Introduce el valor de la posición [fila 2, columna 1]: "))
    d = int(input("Introduce el valor de la posición [fila 2, columna 2]: "))
    
    # Construimos la matriz con los datos que ha metido el usuario
    matriz = np.array([
        [a, b],
        [c, d]
    ])∫
    
    # Para calcular el determinante
    determinante = np.linalg.det(matriz)
    
    # Usamos round(..., 2) para redondear a 2 decimales y limpiar el "error de máquina"
    return round(determinante, 2)

######
##3