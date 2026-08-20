from modules.matrices import calcular_determinante

def main():
    print("=== 🧮 Math & Utility CLI Suite ===")
    
    # Llamamos a nuestra función de matrices
    resultado = calcular_determinante()
    
    # Mostramos el resultado final
    print(f"El determinante es: {resultado}")

if __name__ == "__main__":
    main()