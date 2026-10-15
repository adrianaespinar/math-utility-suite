def menu_bayes():
    try:
        print("\n--- CALCULADORA BAYESIANA ---")
        print("Introduce las probabilidades en formato decimal (ejemplo: 0.10 para 10%)\n")
        
        p_a = float(input("1. Probabilidad a priori (P(A)): "))
        p_b_dado_a = float(input("2. Probabilidad de la evidencia si la teoría es CIERTA (P(B|A)): "))
        p_b_dado_no_a = float(input("3. Probabilidad de la evidencia si la teoría es FALSA (P(B|No A)): "))
        
        # Calculamos la probabilidad de que la teoría sea falsa de base (P(No A))
        p_no_a = 1 - p_a  
        
        # Numerador: La intersección real
        numerador = p_b_dado_a * p_a
        
        # Denominador: La probabilidad total de que ocurra la evidencia
        denominador = numerador + (p_b_dado_no_a * p_no_a)
        
        # Resultado final (Probabilidad a posteriori)
        p_a_dado_b = numerador / denominador
        
        print("\n--- RESULTADO ACTUALIZADO ---")
        print(f"Probabilidad a posteriori: {p_a_dado_b * 100:.2f}%")
        
    except ValueError:
        print("\n❌ Error: Por favor, introduce solo números (usa el punto para los decimales).")