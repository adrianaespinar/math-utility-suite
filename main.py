from modules.matrices import calcular_determinante

def main():
    print("=== 🧮 Math & Utility CLI Suite ===")
    print("Calculando el determinante de la matriz de prueba...")
    
    # Llamamos a la función que guardamos en el otro archivo
    resultado = calcular_determinante()
    
    # Mostramos el resultado en la pantalla
    print(f"El determinante es: {resultado}")

# Esta línea le dice a Python: "ejecuta la función main cuando arranque el archivo"
if __name__ == "__main__":
    main()