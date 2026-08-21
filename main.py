from modules.matrices import menu_matrices

def main():
    print("=======================================")
    print("   🚀 MATH & UTILITY SUITE - CLI       ")
    print("=======================================")
    print("¿Qué área de las matemáticas quieres explorar hoy?")
    print("1. 🧮 Matrices")
    print("2. 📈 Integrales (Próximamente)")
    
    opcion = input("Escribe el número de tu opción: ")
    
    if opcion == "1":
        menu_matrices()
    elif opcion == "2":
        print("🚧 Módulo de integrales en construcción. ¡Pronto lo programaremos!")
    else:
        print("❌ Opción no válida.")

if __name__ == "__main__":
    main()