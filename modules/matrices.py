import numpy as np

def calcular_determinante():
    print("\n--- 🧮 Cálculo de Determinante (Matriz 2x2) ---")
    
    # Pedimos los números uno a uno usando input() y los convertimos a entero con int()
    a = int(input("Introduce el valor de la posición [fila 1, columna 1]: "))
    b = int(input("Introduce el valor de la posición [fila 1, columna 2]: "))
    c = int(input("Introduce el valor de la posición [fila 2, columna 1]: "))
    d = int(input("Introduce el valor de la posición [fila 2, columna 2]: "))
    
    # Construimos la matriz con los datos que ha metido el usuario
    matriz = np.array([
        [a, b],
        [c, d]
    ])
    
    # Calculamos el determinante
    determinante = np.linalg.det(matriz)
    
    # Usamos round(..., 2) para redondear a 2 decimales y limpiar el "error de máquina"
    return round(determinante, 2)