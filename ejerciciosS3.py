# Instrucciones: Evalúa cada expresión y predice el resultado antes de ejecutarlo en Python.

#1. Calcula el resultado de la siguiente operación: 
"""
El resultado de la operación 1 es: 25 + 10 - 5 * 2 para mi es 25, porque primero se realiza la multiplicación (5 * 2 = 10),
luego se suma (25 + 10 = 35) y finalmente se resta (35 - 10 = 25). Esto por la prioridad de las operaciones matemáticas,
donde la multiplicación se realiza antes que la suma y la resta.
"""

resultado1 = 25 + 10 - 5 * 2
print("Resultado de la operación 1:", resultado1)


# 2. Determina el residuo de la división de 23 entre 4
"""
El operador % se utiliza para obtener el residuo de una división. En este caso,
al dividir 23 entre 4, el cociente es 5 (porque 4 * 5 = 20)
y el residuo es 3 (porque 23 - 20 = 3). Por lo tanto, el resultado de la operación es 3.
"""

residuo = 23 % 4
print("El residuo de la división de 23 entre 4 es:", residuo)

# 3. ¿Cuál es el resultado de la división entera entre 55 y 6?
"""
La división entera se realiza utilizando el operador // en Python.
Al dividir 55 entre 6, el resultado de la división entera es 9,
"""
division_entera = 55 // 6
print("El resultado de la división entera entre 55 y 6 es:", division_entera)

# 4. Evalúa el valor de a después de la operación siguiente
"""
El resultado de la operación es 17. Primero se realiza la multiplicación (5 * 2 = 10),
luego se suma (7 + 10 = 17).
"""

a = 7
a = a + 5 * 2
print("El valor de a después de la operación es:", a)   

# 5. Aplica la exponenciación para calcular 4^3
"""
La exponenciación se realiza utilizando el operador ** en Python. Al calcular 4^3,
el resultado es 64, porque 4 elevado a la potencia de 3 es igual a 4 * 4 * 4 = 64.
"""
exponente = 4 ** 3
print("El resultado de 4^3 es:", exponente)

# 6. ¿Cuál es el resultado de la siguiente operación (10 + 2) * 3 - 4 / 2? 
"""
El resultado de la operación 34 es: Primero se realiza la operación dentro de los paréntesis (10 + 2 = 12),
luego se multiplica (12 * 3 = 36), luego nos queda 12 * 3 - 4 / 2, donde se realiza la división (4 / 2 = 2)
y finalmente se resta (36 - 2 = 34). Esto porque la multiplicación y la división tienen mayor prioridad que la suma y la resta,
pero al estar en la misma linea se realizan de izquierda a derecha,
y las operaciones dentro de los paréntesis se realizan primero.
"""

resultado2 = (10 + 2) * 3 - 4 / 2
print("El resultado de la operación 2 es:", resultado2)

# 7. Evalúa la operación con prioridad entre división y multiplicación: 20 / 5 * 2
"""
El resultado de la operación es 8. Primero se realiza la división (20 / 5 = 4),
luego se multiplica (4 * 2 = 8). Esto porque la división y la multiplicación tienen la misma prioridad,
pero se realizan de izquierda a derecha.
"""
resultado3 = 20 / 5 * 2
print("El resultado de la operación con prioridad entre división y multiplicación es:", resultado3)

# 8. Calcula el área de un rectángulo de base 12 y altura 8
"""
El área de un rectángulo se calcula multiplicando la base por la altura.
En este caso,el área es 96, porque 12 * 8 = 96.
"""
altura = 8
base = 12

area_rectangulo = base * altura
print("El área de un rectángulo de base 12 y altura 8 es:", area_rectangulo)   

# 9. Convierte 100 grados Celsius a Fahrenheit con la fórmula F = C * 9/5 + 32

C = 100
F = C * 9 / 5 + 32
print("100 grados Celsius en Fahrenheit es:", F)

# 10. Calcula el perímetro de un triángulo cuyos lados miden 5, 7 y 9.
 
lado1 = 5
lado2 = 7
lado3 = 9

perimetro_triangulo = lado1 + lado2 + lado3
print("El perímetro de un triángulo cuyos lados miden 5, 7 y 9 es:", perimetro_triangulo)

# Ejercicios de Operadores Lógicos
# Instrucciones: Determina si cada expresión retorna True o False.

# 1. ¿El número 10 es mayor que 5 y menor que 20?
print("El resultado de 10 > 5 and 10 < 20 es:", 10 > 5 and 10 < 20)  # True

# 2. Evalúa si False y True devuelven True o False
comparacionlogica = False and True
print("La comparación lógica es entre False y True:", comparacionlogica)  # False)

# 3. Verifica si 15 es múltiplo de 3 o de 4
multiplo3 = 15 % 3 == 0
multiplo4 = 15 % 4 == 0

print("El resultado de comprobar si 15 es multipo de 3 es:", multiplo3)  # True
print("El resultado de comprobar si 15 es multipo de 4 es:", multiplo4)  # False

# 4. ¿El número 8 no es menor que 6?
resultado4 = not (8 < 6)
print("El resultado de comprobar si 8 NO es menor que 6 es:", resultado4)  # True

# 5. Evalúa si 25 es mayor que 10 y 25 no es igual a 30
resultado5 = 25 > 10 and 25 != 30
print("El resultado de comprobar si 25 es mayor que 10 y no es igual a 30 es:", resultado5)  # True

# 6. ¿La suma de 3 y 5 es igual a 8 y 2 por 4 también es 8?
operacion1 = 3 + 5
operacion2 = 2 * 4
resultado6 = operacion1 == 8 and operacion2 ==8
print("El resultado de comprobar si la suma de 3 y 5 es igual a 8 y 2 por 4 es igual a 8 es:", resultado6)  # True

# 7. Evalúa si not True or False devuelve True
evaluacion1 = not True or False
print("El resultado de evaluar not True or False es:", evaluacion1)  # False

# 8. ¿El número 20 es mayor que 18 y menor que 25, pero no igual a 22?
evaluacion2 = 20 > 18 and 20 <25 and 20 != 22
print("El resultado de evaluar si 20 es mayor que 18, menor que 25 y no igual a 22 es:", evaluacion2)  # True

# 9. ¿El número 9 es par o impar? (Usa or) 
"""
No es neccesario usar OR para evaluar si el número 9 es par o impar,
si lo uso como en la primera comprobacion (9 % 2 == 0 or 9 % 2 > 0) el resultado es True, porque 1 de las dos condiciones con OR se cumple,
pero si validamos 9 % 2, el resultado es 1, lo que indica que el número 9 es impar, por lo tanto no es necesario usar OR para evaluar si un número es par o impar
"""

comprobacion1 = 9 % 2 == 0 or 9 % 2 > 0
comprobacion2 = 9 % 2

print("Comprobacion con OR (9 % 2 == 0 or 9 % 2 > 0): ", comprobacion1)  # True
print("Comprobacion sin OR (9 % 2): ", comprobacion2)  # 1 (impar)

# 10. ¿La expresión not (10 > 5 and 2 < 3) devuelve False?
evaluacion3 = not (10 > 5 and 2 < 3)
print("El resultado de evaluar not (10 > 5 and 2 < 3) es:", evaluacion3)  # False
