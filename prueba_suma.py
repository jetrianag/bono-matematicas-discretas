# Programa de prueba: Suma simple

def sumar(a, b):
    """
    Función que suma dos números
    
    Args:
        a: primer número
        b: segundo número
    
    Returns:
        La suma de a + b
    """
    return a + b


# Ejemplos de uso
if __name__ == "__main__":
    print("=== PROGRAMA DE PRUEBA: SUMA ===\n")
    
    # Test 1
    resultado1 = sumar(5, 3)
    print(f"Prueba 1: 5 + 3 = {resultado1}")
    
    # Test 2
    resultado2 = sumar(10, 20)
    print(f"Prueba 2: 10 + 20 = {resultado2}")
    
    # Test 3
    resultado3 = sumar(100, 50)
    print(f"Prueba 3: 100 + 50 = {resultado3}")
    
    print("\n✅ Programa funcionando correctamente")