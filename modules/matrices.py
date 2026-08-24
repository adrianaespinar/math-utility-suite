import numpy as np

# Bloque Limpio


def menu_matrices():
    print("\n--- DEPARTAMENTO DE MATRICES ---")
    print("1. Calcular determinante (2x2 o 3x3)")
    print("2. Calcular Traspuesta (A^T)")
    print("3. Estudiar Simetría/Antisimetría")
    print("4. Suma de matrices")
    print("5. Resta de matrices")
    print("6. Producto por un escalar (K · A )")
    print("7. Multiplicación de matrices (A · B)")
    print("8. Potencia de una matriz ")
    print("9. Calcular la matriz inversa (A^-1)")
    
    opcion = input("Elige qué operación de matrices quieres hacer (1, 2, 3...): ")
    
    if opcion == "1":
        calcular_determinante()
    elif opcion == "2":
        calcular_transpuesta()  
    elif opcion == "3":
        estudiar_simetria()  
    elif opcion == "4":
        suma_matrices()
    elif opcion == "5":
        resta_matrices()
    elif opcion == "6":
        producto_por_escalar()
    elif opcion == "7":
        multiplicar_matrices()
    elif opcion == "8": 
        potencia_matriz()
    elif opcion == "9":
        matriz_inversa()
    else:
      print(" Opción de matrices no válida.")


def suma_matrices(): # m y n deben de ser identicas
    print("\n--- Suma de Matrices ---")
    
    print("Dimensiones de la Matriz A:")
    m_a = int(input("Filas de A (m): "))
    n_a = int(input("Columnas de A (n): "))
    
    print("Dimensiones de la Matriz B:")
    m_b = int(input("Filas de B (m): "))
    n_b = int(input("Columnas de B (n): "))
    
    # Comprobar tamaño para sumar
    if m_a != m_b or n_a != n_b:
        print(" Error: Para sumar dos matrices, AMBAS deben tener exactamente las mismas dimensiones (mismo número de filas y columnas)")
        return

    print("Introduce los elementos de la matriz A:") 
    filas_a= [] 
    for i in range(m_a):
        fila = []
        for j in range(n_a):
            valor = int(input(f "Matriz A - Fila {i+1}, Columna {j+1}"))
            fila.append(valor)
        filas_a.append(fila)


    print("Introduce los elementos de la matriz B:")  

    return

def resta_matrices():
    return

def producto_por_escalar():
    return

def multiplicar_matrices():
    return

def potencia_matriz():
    return

def matriz_inversa():
    return


    

def calcular_transpuesta():
    print("\n--- Cálculo de la Traspuesta ---")
    
   
    m = int(input("¿Cuántas filas tiene la matriz? (m): ")) 
    n = int(input("¿Cuántas columnas tiene la matriz? (n): "))
    
    print(f"Introduce los elementos fila por fila:")
    
    # (se adapta a m y n automáticamente)
    filas = []
    for i in range(m):
        fila = []
        for j in range(n):
            valor = int(input(f"Elemento Fila {i+1}, Columna {j+1}: "))
            fila.append(valor)
        filas.append(fila)
        
    matriz = np.array(filas)
    
    transpuesta = matriz.T

    print("\n--- Resultados ---")
    print("Matriz original (A):\n", matriz)
    print("\nMatriz Traspuesta (A^T):\n", transpuesta)
    
    return transpuesta



def estudiar_simetria():
    print("\n--- Estudio de Simetría y Antisimetría ---")
    
    m = int(input("Indica el número de filas (m): "))
    n = int(input("Indica el número de columnas (n): "))
    
    if m != n:
        print(" Error: Para estudiar la simetría o antisimetría, la matriz TIENE que ser cuadrada (mismo número de filas y columnas).")
        return # Para frenar la función 
        
    print("Introduce los elementos fila por fila:")
    filas = []
    for i in range(m):
        fila = []
        for j in range(n):
            valor = int(input(f"Elemento Fila {i+1}, Columna {j+1}: "))
            fila.append(valor)
        filas.append(fila)
        
    matriz = np.array(filas)
    transpuesta = matriz.T #El nombre matriz viene de la linea anterior, establecemos variable "matriz", se podria poner cualquiera. 
                           # El .T es de numpy para calcular la transpuesta


    # RESULTADOS Estudio Simetria
    print("\n--- Resultados del Análisis ---")
    print("Matriz A:\n", matriz)
    print("\nMatriz Traspuesta (A^T):")
    print(transpuesta)
    
    # Comprobación 
    es_simetrica = np.array_equal(matriz, transpuesta)
    es_antisimetrica = np.array_equal(matriz, -transpuesta)
    
    if es_simetrica:
        print("\n ¡La matriz es Simétrica (Cumple que A = A^T)")
    elif es_antisimetrica:
        print("\n ¡La matriz es Antisimétrica (Cumple que A = -A^T)")
    else:
        print("\n La matriz es cuadrada, pero no es ni simétrica ni antisimétrica.")










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



