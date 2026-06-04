def factorial(n):
    """Calcula el factorial de n"""
    if n < 0:
        return 0
    if n == 0 or n == 1:
        return 1
    
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def permutacion(n, r):
    """Calcula P(n,r) = n! / (n-r)!"""
    if r > n or r < 0:
        return 0
    return factorial(n) // factorial(n - r)

def problema_1():
    
    print("\n--- Problema 1: Permutaciones y K-Permutaciones ---")
    
    # Validar n
    n = input("\nIngrese n: ")
    while True:
        if not n.isdigit():
            print("Debe ingresar un número")
            n = input("Ingrese n: ")
        elif int(n) < 0:
            print("n debe ser no negativo (≥ 0)")
            n = input("Ingrese n: ")
        else:
            n = int(n)
            break
    
    # Validar r
    r = input("Ingrese r: ")
    while True:
        if not r.isdigit():
            print("Debe ingresar un número")
            r = input("Ingrese r: ")
        elif int(r) < 0:
            print("r debe ser no negativo (≥ 0)")
            r = input("Ingrese r: ")
        elif int(r) > n:
            print(f"r no puede ser mayor que n ({n})")
            r = input("Ingrese r: ")
        else:
            r = int(r)
            break
    
    # Calcular permutación
    factorial_n = factorial(n)
    factorial_n_menos_r = factorial(n - r)
    permutacion = factorial_n // factorial_n_menos_r
    
    # Mostrar resultados
    print("="*40)
    print(f"n = {n}")
    print(f"r = {r}")
    print("="*40)
    print(f"n! = {factorial_n}")
    print(f"(n-r)! = {factorial_n_menos_r}")
    print(f"P({n},{r}) = {n}! / ({n}-{r})! = {permutacion}")
    print("="*40)

def problema_4():
    
    print("\n--- Problema 2: Sistema de conteo de contraseñas ---")
    
    # 1. VALIDAR LONGITUD n
    n = input("\nIngrese longitud n (máximo 50): ")
    while True:
        if not n.isdigit():
            print("Debe ingresar un número")
            n = input("Ingrese longitud n (máximo 50): ")
        elif int(n) <= 0:
            print("n debe ser mayor a 0")
            n = input("Ingrese longitud n (máximo 50): ")
        elif int(n) > 50:
            print("n debe ser máximo 50")
            n = input("Ingrese longitud n (máximo 50): ")
        else:
            n = int(n)
            break
    
    # 2. VALIDAR TAMAÑO ALFABETO
    alfabeto = input("Ingrese tamaño del alfabeto (máximo 27): ")
    while True:
        if not alfabeto.isdigit():
            print("Debe ingresar un número")
            alfabeto = input("Ingrese tamaño del alfabeto (máximo 27): ")
        elif int(alfabeto) < 0:
            print("alfabeto no puede ser negativo")
            alfabeto = input("Ingrese tamaño del alfabeto (máximo 27): ")
        elif int(alfabeto) > 27:
            print("alfabeto debe ser máximo 27")
            alfabeto = input("Ingrese tamaño del alfabeto (máximo 27): ")
        else:
            alfabeto = int(alfabeto)
            break
    
    # 3. VALIDAR PERMITE REPETICIÓN
    repeticion = input("¿Permite repetición? (1=Sí, 2=No): ")
    while True:
        if not repeticion.isdigit():
            print("Debe ingresar 1 o 2")
            repeticion = input("¿Permite repetición? (1=Sí, 2=No): ")
        elif int(repeticion) not in [1, 2]:
            print("Ingrese 1 (Sí) o 2 (No)")
            repeticion = input("¿Permite repetición? (1=Sí, 2=No): ")
        else:
            repeticion = int(repeticion)
            break
    
    # 4. VALIDACIÓN DE IMPOSIBILIDAD
    if repeticion == 2:
        alfabeto_total_maximo = (alfabeto * 2) + 10 + 10
        while n > alfabeto_total_maximo:
            print(f"Imposible: necesita {n} caracteres diferentes pero solo tiene {alfabeto_total_maximo} disponibles")
            
            n = input("Ingrese longitud n (máximo 50): ")
            while True:
                if not n.isdigit():
                    print("Debe ingresar un número")
                    n = input("Ingrese longitud n (máximo 50): ")
                elif int(n) <= 0:
                    print("n debe ser mayor a 0")
                    n = input("Ingrese longitud n (máximo 50): ")
                elif int(n) > 50:
                    print("n debe ser máximo 50")
                    n = input("Ingrese longitud n (máximo 50): ")
                else:
                    n = int(n)
                    break
            
            alfabeto = input("Ingrese tamaño del alfabeto (máximo 27): ")
            while True:
                if not alfabeto.isdigit():
                    print("Debe ingresar un número")
                    alfabeto = input("Ingrese tamaño del alfabeto (máximo 27): ")
                elif int(alfabeto) < 0:
                    print("alfabeto no puede ser negativo")
                    alfabeto = input("Ingrese tamaño del alfabeto (máximo 27): ")
                elif int(alfabeto) > 27:
                    print("alfabeto debe ser máximo 27")
                    alfabeto = input("Ingrese tamaño del alfabeto (máximo 27): ")
                else:
                    alfabeto = int(alfabeto)
                    break
            
            alfabeto_total_maximo = (alfabeto * 2) + 10 + 10
    
    # 5. MENÚ DE RESTRICCIÓN
    print("\n" + "="*40)
    print("OPCIONES DE RESTRICCIÓN:")
    print("0 = Sin restricción")
    print("1 = Al menos un dígito obligatorio (0-9)")
    print("2 = Al menos una mayúscula obligatoria")
    print("3 = Al menos un símbolo especial (!@#$%^&*())")
    print("="*40)
    
    restriccion = input("Seleccione restricción (0, 1, 2 o 3): ")
    while True:
        if not restriccion.isdigit():
            print("Debe ingresar 0, 1, 2 o 3")
            restriccion = input("Seleccione restricción (0, 1, 2 o 3): ")
        elif int(restriccion) not in [0, 1, 2, 3]:
            print("Ingrese 0, 1, 2 o 3")
            restriccion = input("Seleccione restricción (0, 1, 2 o 3): ")
        else:
            restriccion = int(restriccion)
            break
    
    # 6. CALCULAR ALFABETO TOTAL
    alfabeto_total = (alfabeto * 2) + 10 + 10
    
    # 7 y 8. CALCULAR TOTAL BASE Y APLICAR RESTRICCIÓN
    if restriccion == 0:  # Sin restricción
        if repeticion == 1:
            resultado = alfabeto_total ** n
        else:
            resultado = permutacion(alfabeto_total, n)
    
    elif restriccion == 1:  # Dígito obligatorio
        if repeticion == 1:
            resultado = (alfabeto_total ** n) - ((alfabeto_total - 10) ** n)
        else:
            resultado = permutacion(alfabeto_total, n) - permutacion(alfabeto_total - 10, n)
    
    elif restriccion == 2:  # Mayúscula obligatoria
        if repeticion == 1:
            resultado = (alfabeto_total ** n) - ((alfabeto_total - alfabeto) ** n)
        else:
            resultado = permutacion(alfabeto_total, n) - permutacion(alfabeto_total - alfabeto, n)
    
    elif restriccion == 3:  # Símbolo obligatorio
        if repeticion == 1:
            resultado = (alfabeto_total ** n) - ((alfabeto_total - 10) ** n)
        else:
            resultado = permutacion(alfabeto_total, n) - permutacion(alfabeto_total - 10, n)
    
    # 9. MOSTRAR RESULTADOS
    print("\n" + "="*50)
    print("RESULTADOS")
    print("="*50)
    print(f"Longitud de contraseña (n): {n}")
    print(f"Tamaño alfabeto (letras): {alfabeto}")
    print(f"Permite repetición: {'Sí' if repeticion == 1 else 'No'}")
    print(f"Restricción: ", end="")
    if restriccion == 0:
        print("Sin restricción")
    elif restriccion == 1:
        print("Al menos un dígito (0-9)")
    elif restriccion == 2:
        print("Al menos una mayúscula")
    elif restriccion == 3:
        print("Al menos un símbolo especial (!@#$%^&*())")
    print("="*50)
    print(f"Alfabeto total: {alfabeto_total} caracteres")
    print(f"  - Letras minúsculas: {alfabeto}")
    print(f"  - Letras mayúsculas: {alfabeto}")
    print(f"  - Dígitos: 10")
    print(f"  - Símbolos especiales: 10")
    print("="*50)
    print(f"Total de contraseñas posibles: {resultado}")
    print("="*50)


def main():
    """Función principal que controla el menú"""
    
    # Mostrar menú una sola vez
    print("\n" + "="*73)
    print("MENÚ PRINCIPAL")
    print("="*73)
    print("1. Programa 1 - Calculadora general de permutaciones y k-permutaciones")
    print("2. Programa 2 - Sistema de conteo de contraseñas con restricciones")
    print("0. Salir")
    print("="*73)
    
    # Único while para pedir opción
    while True:
        opcion = input("\nIngrese una opción (0, 1 o 2): ").strip()
        
        if opcion not in ['0', '1', '2']:
            print("Opción inválida, ingrese 0, 1 o 2")
            continue
        
        opcion = int(opcion)
        
        # Ejecutar según la opción
        if opcion == 1:
            problema_1()
        
        elif opcion == 2:
            problema_4()
        
        if opcion == 0:
            print("\nPrograma terminado. ¡Gracias por usar!")
            break

if __name__ == "__main__":
    main()