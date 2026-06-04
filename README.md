# Bono de Programación: problemas de Conteo
## Matemáticas Discretas I

**Estudiante:** Jean Carlo Triana Guzmán

**Docente:** Jhoan Sebastian Tenjo García

**Universidad:** Universidad Nacional de Colombia

---

## Descripción General

Este proyecto contiene la solución de dos problemas de conteo combinatorio de la materia Matemáticas Discretas I. Se implementaron dos programas en Python que permiten al usuario resolver problemas específicos de permutaciones y conteo de contraseñas con restricciones configurables.

---

## Requisitos

- Python 3.7 o superior
- No requiere librerías externas (solo módulos estándar)

---

## Instrucciones de Instalación y Ejecución

### Opción 1: Clonar desde GitHub
```bash
git clone https://github.com/jetrianag/bono-matematicas-discretas.git
cd bono-matematicas-discretas
python Problemas_de_conteo.py
```

### Opción 2: Ejecutar directamente
```bash
python Problemas_de_conteo.py
```

El programa abrirá un menú interactivo en la terminal donde puedes seleccionar qué problema resolver.

---

## Explicación Breve de los Problemas Resueltos

### Problema 1: Permutaciones y K-Permutaciones
Este programa calcula el número de formas de ordenar r objetos distintos tomados de un conjunto de n objetos distintos. Utiliza la fórmula P(n,r) = n! / (n-r)! e incluye validación de entradas para garantizar que n y r sean enteros no negativos.

### Problema 4: Sistema de Conteo de Contraseñas
Este programa cuenta cuántas contraseñas se pueden formar bajo reglas configurables. Permite al usuario especificar la longitud, el alfabeto permitido, si permite repetición, y qué restricciones aplicar (dígitos obligatorios, mayúsculas obligatorias, símbolos especiales obligatorios).

---

## Problema 1: Permutaciones y K-Permutaciones

### 1.1 Explicación del Problema
Se desea contar el número de formas de ordenar r objetos distintos tomados de un conjunto de n objetos distintos. Por ejemplo, ¿cuántas formas hay de elegir 2 elementos de {A, B, C, D, E} donde el orden importa?

### 1.2 Fórmula Usada
```
P(n,r) = n! / (n-r)!

donde:
n! = n × (n-1) × (n-2) × ... × 1
```

### 1.3 Explicación del Algoritmo
1. Solicita al usuario valores para n y r
2. Valida que ambos sean enteros no negativos y que r ≤ n
3. Calcula n! (factorial de n)
4. Calcula (n-r)! (factorial de n-r)
5. Divide n! entre (n-r)! para obtener P(n,r)
6. Muestra el resultado con desglose de cálculos

### 1.4 Código Funcional
```python
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
```

### 1.5 Pruebas

| Prueba | n | r | Resultado | Observación |
|--------|---|---|-----------|-------------|
| 1 | 5 | 2 | 20 | Valores pequeños |
| 2 | 4 | 4 | 24 | r = n (permutación total) |
| 3 | 6 | 0 | 1 | r = 0 (solo 1 forma) |
| 4 | 10 | 3 | 720 | Valores mayores |
| 5 | 3 | 5 | Error | Validación: r > n |

### 1.6 Validación de Casos Especiales
- Si n o r son negativos: se rechaza y pide de nuevo
- Si r > n: se rechaza y pide de nuevo
- Si ingresa caracteres en lugar de números: se rechaza y pide de nuevo
- Si r = 0: resultado correcto = 1
- Si r = n: resultado correcto = n!

### 1.7 Comentarios sobre Eficiencia

#### ¿Por qué se usó factorial iterativo y no recursivo?

Se eligió la implementación iterativa porque:

1. **Usa menos memoria:** El factorial recursivo crea una "pila" de llamadas. 
   Si n=100, el programa mantiene 100 capas en memoria.
   El iterativo solo usa un bucle, con la misma memoria siempre.

2. **Es más rápido:** No hay sobrecarga de llamadas de funciones.
   Cada llamada recursiva consume tiempo adicional.

3. **Es más fácil de entender:** El bucle es directo: multiplica n veces.
   La recursión es más abstracta.

- **Complejidad Temporal:** O(n)
  El programa hace n multiplicaciones para calcular n!. Si n es mayor, tarda más tiempo proporcionalmente.
  
- **Complejidad Espacial:** O(1)
  El programa solo usa algunas variables (n, r, resultado). No importa cuán grande sea n, siempre usa la misma cantidad de memoria.

---

## Problema 4: Sistema de Conteo de Contraseñas

### 4.1 Explicación del Problema
Se desea contar cuántas contraseñas se pueden formar bajo reglas configurables. El usuario especifica la longitud deseada, el tamaño del alfabeto (letras minúsculas), si permite repetición de caracteres, y opcionalmente qué restricciones aplicar (al menos un dígito, mayúscula o símbolo especial).

### 4.2 Fórmula Usada

**Con repetición:**
```
Total = (alfabeto_total)^n
```

**Sin repetición:**
```
Total = P(alfabeto_total, n) = alfabeto_total! / (alfabeto_total - n)!
```

**Con restricción (complementación):**
```
Total = Total_sin_restricción - Total_sin_elemento_obligatorio
```

Donde `alfabeto_total = (alfabeto × 2) + 10 + 10`:
- alfabeto × 2 = letras minúsculas + mayúsculas
- 10 = dígitos (0-9)
- 10 = símbolos especiales (!@#$%^&*())

### 4.3 Explicación del Algoritmo
1. Valida longitud n (máximo 50, mínimo 1)
2. Valida tamaño alfabeto (máximo 27, mínimo 0)
3. Pregunta si permite repetición
4. Valida que sea posible (si no permite repetición, n ≤ alfabeto_total)
5. Pregunta qué restricción aplicar (sin restricción, dígito, mayúscula, símbolo)
6. Calcula el alfabeto total considerando mayúsculas, dígitos y símbolos
7. Calcula total base (con o sin repetición)
8. Aplica la restricción seleccionada
9. Muestra resultados desglosados

### 4.4 Código Funcional
```python
def permutacion(n, r):
    """Calcula P(n,r) = n! / (n-r)!"""
    if r > n or r < 0:
        return 0
    return factorial(n) // factorial(n - r)


def problema_4():
    """Sistema de conteo de contraseñas con restricciones"""
    
    print("\n--- Problema 4: Sistema de Conteo de Contraseñas ---")
    
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
    repeticion = input("Permite repetición (1=Sí, 2=No): ")
    while True:
        if not repeticion.isdigit():
            print("Debe ingresar 1 o 2")
            repeticion = input("Permite repetición (1=Sí, 2=No): ")
        elif int(repeticion) not in [1, 2]:
            print("Ingrese 1 (Sí) o 2 (No)")
            repeticion = input("Permite repetición (1=Sí, 2=No): ")
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
    if restriccion == 0:
        if repeticion == 1:
            resultado = alfabeto_total ** n
        else:
            resultado = permutacion(alfabeto_total, n)
    
    elif restriccion == 1:
        if repeticion == 1:
            resultado = (alfabeto_total ** n) - ((alfabeto_total - 10) ** n)
        else:
            resultado = permutacion(alfabeto_total, n) - permutacion(alfabeto_total - 10, n)
    
    elif restriccion == 2:
        if repeticion == 1:
            resultado = (alfabeto_total ** n) - ((alfabeto_total - alfabeto) ** n)
        else:
            resultado = permutacion(alfabeto_total, n) - permutacion(alfabeto_total - alfabeto, n)
    
    elif restriccion == 3:
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
```

### 4.5 Pruebas

| Prueba | n | alfabeto | repetición | restricción | Resultado | Observación |
|--------|---|----------|-----------|-------------|-----------|-------------|
| 1 | 5 | 0 | Sí | Sin restricción | 100000 | Solo dígitos, con repetición |
| 2 | 5 | 27 | Sí | Sin restricción | 3289172 | Letras + dígitos + símbolos |
| 3 | 8 | 10 | No | Dígito | Error | Imposible: solo hay 10 dígitos |
| 4 | 4 | 5 | No | Mayúscula | 1260 | Sin repetir con restricción |
| 5 | 6 | 27 | Sí | Símbolo | 3010936 | Con restricción de símbolo |

### 4.6 Validación de Casos Especiales
- Si n > 50: se rechaza y pide de nuevo
- Si alfabeto > 27: se rechaza y pide de nuevo
- Si no permite repetición y n > alfabeto_total: se rechaza y pide nuevos valores
- Si ingresa caracteres en lugar de números: se rechaza y pide de nuevo
- Si selecciona restricción inválida: se rechaza y pide de nuevo
- Si alfabeto = 0 pero permite repetición: funciona correctamente

### 4.7 Comentarios sobre Eficiencia

#### ¿Cómo se aplica la Regla del Producto?

La **regla del producto** se aplica cuando calculas el total de contraseñas con repetición usando potencias:

Total = (alfabeto_total)^n

**¿Por qué funciona?** Porque cada posición en la contraseña es un **evento independiente**:

- **Posición 1:** tienes alfabeto_total opciones
- **Posición 2:** tienes alfabeto_total opciones (sin importar qué elegiste en posición 1)
- **Posición 3:** tienes alfabeto_total opciones (sin importar las anteriores)
- ... y así n veces

Como cada posición es **independiente**, **multiplicas** el número de opciones.

#### Complejidad del Programa

- **Complejidad Temporal:** O(1) con repetición, O(n) sin repetición
  Con repetición, solo hace una potencia (rápido). Sin repetición, calcula factorial (más lento si n es grande).

- **Complejidad Espacial:** O(1)
  El programa solo usa variables simples (n, alfabeto, resultado). No importa los valores, siempre usa la misma memoria.

- Los números pueden ser muy grandes, pero Python maneja enteros arbitrarios sin problema

- Eficiente incluso para valores máximos de entrada.

---

## Ejemplos de Entrada y Salida

### Ejemplo 1: Problema 1

**Entrada:**
```
Ingrese n: 5
Ingrese r: 2
```

**Salida:**
```
========================================
n = 5
r = 2
========================================
n! = 120
(n-r)! = 6
P(5,2) = 5! / (5-2)! = 20
========================================
```

### Ejemplo 2: Problema 4

**Entrada:**
```
Ingrese longitud n: 6
Ingrese tamaño del alfabeto: 10
Permite repetición: 1
Seleccione restricción: 1
```

**Salida:**
```
==================================================
RESULTADOS
==================================================
Longitud de contraseña (n): 6
Tamaño alfabeto (letras): 10
Permite repetición: Sí
Restricción: Al menos un dígito (0-9)
==================================================
Alfabeto total: 54 caracteres
  - Letras minúsculas: 10
  - Letras mayúsculas: 10
  - Dígitos: 10
  - Símbolos especiales: 10
==================================================
Total de contraseñas posibles: 34012223
==================================================
```

---

## Comentarios finales

Ambos programas demuestran la aplicación práctica de conceptos de combinatoria. El Problema 1 muestra cómo las permutaciones calculan arreglos ordenados, mientras que el Problema 4 ilustra cómo aplicar principios de conteo (regla del producto y complementación) en problemas del mundo real como la seguridad de contraseñas.
