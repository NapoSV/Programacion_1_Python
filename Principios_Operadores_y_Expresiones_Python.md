# Principios Básicos de Operadores y Expresiones en Python

Este documento explica los **principios fundamentales** que se utilizan en el archivo `ejerciciosS3.py`, con ejemplos claros y explicaciones conceptuales.

---

## 1. Prioridad de Operaciones (Orden de Precedencia)

Python respeta las reglas matemáticas tradicionales:

1. Paréntesis `()`
2. Exponenciación `**`
3. Multiplicación `*`, División `/`, División entera `//` y Módulo `%`
4. Suma `+` y Resta `-`

**Ejemplo:**
```python
25 + 10 - 5 * 2
```
Primero se realiza la multiplicación (`5 * 2`), luego la suma y resta.

---

## 2. Operador Módulo (%)

El operador `%` devuelve el **residuo** de una división.

**Ejemplo:**
```python
23 % 4  # resultado: 3
```

Se utiliza frecuentemente para saber si un número es **par o impar**.

---

## 3. División Entera (//)

La división entera devuelve solo la **parte entera** del cociente.

**Ejemplo:**
```python
55 // 6  # resultado: 9
```

---

## 4. Asignación con Expresiones

Una variable puede actualizar su valor usando su valor anterior.

**Ejemplo:**
```python
a = a + 5 * 2
```

Primero se resuelve la multiplicación y luego se suma.

---

## 5. Exponenciación (**)

El operador `**` permite elevar un número a una potencia.

**Ejemplo:**
```python
4 ** 3  # resultado: 64
```

---

## 6. Uso de Paréntesis

Los paréntesis alteran el orden natural de las operaciones.

**Ejemplo:**
```python
(10 + 2) * 3 - 4 / 2
```

Primero se evalúa lo que está dentro de los paréntesis.

---

## 7. Operaciones del Mismo Nivel

Cuando multiplicación y división tienen la misma prioridad, se evalúan **de izquierda a derecha**.

**Ejemplo:**
```python
20 / 5 * 2  # resultado: 8
```

---

## 8. Aplicación Matemática: Área de un Rectángulo

Las fórmulas matemáticas se trasladan directamente a Python.

**Ejemplo:**
```python
area = base * altura
```

---

## 9. Conversión de Temperaturas

Python permite aplicar fórmulas físicas fácilmente.

**Fórmula:**
```
F = C * 9/5 + 32
```

---

## 10. Suma de Valores: Perímetro

El perímetro se obtiene sumando todos los lados.

**Ejemplo:**
```python
perimetro = lado1 + lado2 + lado3
```

---

# Operadores Lógicos en Python

## 11. Operador AND

`and` devuelve `True` solo si **todas** las condiciones son verdaderas.

```python
10 > 5 and 10 < 20
```

---

## 12. Operador OR

`or` devuelve `True` si **al menos una** condición es verdadera.

```python
9 % 2 == 0 or 9 % 2 > 0
```

---

## 13. Operador NOT

`not` invierte el valor lógico.

```python
not (8 < 6)
```

---

## 14. Comparaciones Lógicas

Python permite comparar valores usando:

- `>` mayor que
- `<` menor que
- `==` igual
- `!=` diferente

---

## 15. Uso Correcto de Operadores Lógicos

Para saber si un número es par o impar **no es necesario usar OR**:

```python
9 % 2 == 0  # par
9 % 2 != 0  # impar
```

---

## Conclusión

Estos principios son la base para:
- Resolver expresiones matemáticas
- Tomar decisiones lógicas
- Comprender cómo Python evalúa instrucciones

Dominar estos conceptos es clave para avanzar en programación 🚀
