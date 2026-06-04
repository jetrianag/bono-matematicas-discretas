# Prompts Utilizados para Asistencia de IA

Este archivo documenta todos los prompts (instrucciones) que se proporcionaron a la inteligencia artificial para el desarrollo de este proyecto. Cada prompt fue específico y detallado, y el código generado fue revisado, entendido y ajustado según sea necesario.

---

## Prompt 1: Estructura del Menú Principal

**Instrucción dada:**

"Crea una función `main()` que implemente un menú interactivo en la terminal. 

El menú debe:
- Mostrar 3 opciones: 1 (Problema 1), 2 (Problema 4), 0 (Salir)
- Usar un while True para repetir
- Si el usuario selecciona 1, ejecutar `problema_1()`
- Si selecciona 2, ejecutar `problema_4()`
- Si selecciona 0, terminar el programa con un mensaje de despedida
- Si selecciona algo diferente, mostrar error y volver a pedir

Usa formato claro con líneas de separación (=====) para hacer el menú legible."

**Resultado:** Función main() que controla el flujo del programa completo.

---

## Prompt 2: Función Factorial Iterativa

**Instrucción dada:**

"Crea una función `factorial(n)` que calcule el factorial de n de forma ITERATIVA (usando un bucle for, no recursiva).

Requisitos:
- Si n < 0, retorna 0
- Si n == 0 o n == 1, retorna 1
- Para n > 1, multiplica todos los números desde 2 hasta n usando un bucle
- Solo usa variables simples, sin llamadas recursivas
- Agrega un docstring explicando qué hace"

**Resultado:** Función factorial() eficiente en memoria y velocidad.

---

## Prompt 3: Validación de Entrada sin Try-Except

**Instrucción dada:**

"Crea un sistema de validación para entrada de datos SIN usar try-except.

Requisitos:
- Pide un número al usuario
- Usa `isdigit()` para verificar que sea un número
- Si no es número, muestra error específico y vuelve a pedir
- Si es número pero está fuera de rango (ej: negativo), muestra error específico y vuelve a pedir
- Usa while True con continue y break

Ejemplo de validación para n (máximo 50, mínimo 1):
- Si no es dígito: 'Debe ingresar un número'
- Si <= 0: 'n debe ser mayor a 0'
- Si > 50: 'n debe ser máximo 50'"

**Resultado:** Sistema robusto de validación en todos los inputs del programa.

---

## Prompt 4: Problema 1 - Calculadora de Permutaciones

**Instrucción dada:**

"Crea la función `problema_1()` que implemente una calculadora de permutaciones.

Requisitos:
1. Pide al usuario valores para n y r
2. Valida ambos usando el sistema isdigit() + while (sin try-except)
3. Verifica que n >= 0, r >= 0, y r <= n
4. Calcula:
   - factorial_n = factorial(n)
   - factorial_n_menos_r = factorial(n - r)
   - permutacion = factorial_n // factorial_n_menos_r
5. Muestra resultados con formato:
   - Los valores de n y r
   - Los factoriales calculados
   - La fórmula P(n,r) = n! / (n-r)!
   - El resultado final
6. Todo separado por líneas de = para claridad"

**Resultado:** Función problema_1() completamente funcional y validada.

---

## Prompt 5: Problema 4 - Sistema de Conteo de Contraseñas (Parte 1)

**Instrucción dada:**

"Crea la función `problema_4()` que cuente contraseñas con restricciones.

PRIMERA PARTE - Validaciones:

1. Pide longitud n (máximo 50, mínimo > 0)
   - Valida sin try-except, usa isdigit()
   - Mensajes específicos de error

2. Pide tamaño alfabeto (máximo 27, mínimo >= 0)
   - Valida sin try-except, usa isdigit()
   - Mensajes específicos de error

3. Pide si permite repetición (1=Sí, 2=No)
   - Solo acepta 1 o 2
   - Si es otra cosa, pide de nuevo

4. VALIDACIÓN CRÍTICA: Si no permite repetición
   - Calcula alfabeto_total_maximo = (alfabeto * 2) + 10 + 10
   - Si n > alfabeto_total_maximo, muestra error
   - Vuelve a pedir n y alfabeto hasta que sea posible"

**Resultado:** Sistema robusto de validaciones para los parámetros iniciales.

---

## Prompt 6: Problema 4 - Sistema de Conteo de Contraseñas (Parte 2)

**Instrucción dada:**

"Continúa con la función `problema_4()`.

SEGUNDA PARTE - Restricciones y Cálculo:

5. Muestra menú de restricciones:
   - 0 = Sin restricción
   - 1 = Al menos un dígito obligatorio (0-9)
   - 2 = Al menos una mayúscula obligatoria
   - 3 = Al menos un símbolo especial (!@#$%^&*())
   - Valida que sea 0, 1, 2 o 3

6. Calcula alfabeto_total = (alfabeto * 2) + 10 + 10
   (Suma: letras minúsculas, mayúsculas, dígitos, símbolos)

7. Calcula según repetición y restricción:
   - SI restricción = 0: resultado = alfabeto_total ^ n (con repetición) 
                         o P(alfabeto_total, n) (sin repetición)
   - SI restricción = 1: resultado = total - (total sin dígitos)
   - SI restricción = 2: resultado = total - (total sin mayúsculas)
   - SI restricción = 3: resultado = total - (total sin símbolos)

8. Muestra resultados desglosados con:
   - Parámetros ingresados
   - Desglose del alfabeto total
   - Resultado final"

**Resultado:** Sistema completo de cálculo de contraseñas con todas las opciones.

---

## Prompt 7: Estructura General del Programa

**Instrucción dada:**

"Organiza el programa completo en este orden:

1. Función `factorial(n)` - al inicio
2. Función `permutacion(n, r)` - después
3. Función `problema_1()` - luego
4. Función `problema_4()` - después
5. Función `main()` - penúltima
6. Bloque `if __name__ == '__main__'` - al final

Asegúrate que:
- Todas las funciones tengan docstrings
- El código sea limpio y legible
- No haya código repetido
- Las variables tengan nombres claros"

**Resultado:** Programa bien estructurado y fácil de mantener.

---

## Prompt 8: Documentación (README)

**Instrucción dada:**

"Crea un README.md completo que incluya:

1. Título y información básica (universidad, docente, estudiante)
2. Descripción general del proyecto
3. Requisitos y instrucciones de ejecución
4. Explicación breve de ambos problemas
5. Para cada problema:
   - Explicación del problema
   - Fórmula usada
   - Explicación del algoritmo
   - Código funcional
   - Al menos 5 pruebas con resultados
   - Validación de casos especiales
   - Comentarios sobre eficiencia
6. Ejemplos de entrada y salida
7. Conclusiones

Usa formato Markdown profesional con títulos, tablas, bloques de código y énfasis."

**Resultado:** Documentación completa y profesional del proyecto.

---

## Resumen

Todos estos prompts fueron diseñados para:
- **Definir claramente** qué se necesitaba
- **Especificar detalles técnicos** (validaciones, formatos, etc.)
- **Acelerar el desarrollo** sin perder calidad
- **Mantener el aprendizaje** ya que cada instrucción fue revisada y entendida

El código generado fue validado, ajustado y se aseguró que funcionara correctamente antes de ser incluido en el proyecto final.