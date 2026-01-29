# 📘 Declaración de Variables en Python

**Registro 1 – Programación 1**  
Documento de ampliación teórica basado en la guía de ejercicios

---

## 🧠 ¿Qué es una variable en Python?

Una **variable** es un nombre que referencia a un valor almacenado en memoria. En Python, las variables:

- No necesitan declarar tipo explícito.
- El tipo se asigna automáticamente según el valor.
- Pueden cambiar de tipo dinámicamente.

Ejemplo:
```python
x = 10      # int
x = "Hola"  # str
x = True    # bool
```

---

## ⚙️ Tipado dinámico

Python es un lenguaje de **tipado dinámico**, lo que significa que:

- El tipo depende del valor, no del nombre de la variable
- El tipo puede cambiar durante la ejecución

```python
x = 5        # int
x = 5.5      # float
x = "texto" # str
```

---

## 📦 Tipos de datos básicos

### 🔢 int (Enteros)

Números sin decimales, positivos o negativos.

```python
numero_entero = 20
numero_negativo_entero = -35
```

Características:
- Precisión ilimitada
- Operaciones aritméticas exactas

---

### 🔣 float (Decimales)

Números con punto decimal.

```python
numero_flotante = 35.33
numero_flotante_negativo = -0.96969
```

Características:
- Representación en coma flotante
- Puede haber errores de precisión

Ejemplo:
```python
0.1 + 0.2  # ≠ 0.3 exactamente
```

---

### 🧵 str (Cadenas de texto)

Texto entre comillas simples o dobles.

```python
cadena_texto = "Programación 1"
cadena_vacia = ""
```

Características:
- Son inmutables
- Soportan concatenación
- Indexables

```python
nombre = "Ana"
apellido = "Lopez"
print(nombre + " " + apellido)
```

---

### 🔘 bool (Booleanos)

Valores lógicos:

```python
True
False
```

Ejemplo:
```python
booleano_verdadero = True
booleano_falso = False
```

Se usan para:
- Condiciones
- Control de flujo
- Lógica booleana

---

## 🔍 Función type()

La función `type()` permite identificar el tipo de dato:

```python
x = 10
print(type(x))
```

Salida:
```
<class 'int'>
```

---

## ⚠️ Importante sobre type() y concatenación

`type()` devuelve un objeto de tipo `type`, no una cadena de texto.

❌ Incorrecto:
```python
print(type(a) + type(b))
```

✅ Correcto:
```python
print(type(a), type(b))
```

O:
```python
print(str(type(a)) + " " + str(type(b)))
```

---

## 📚 Asignación múltiple

```python
a, b, c = 1, 2.5, "texto"
```

---

## 🔄 Reasignación

```python
x = 10
x = "Hola"
```

Python no genera error por cambio de tipo.

---

## 🧩 Convenciones de nombres

Buenas prácticas:

- snake_case
- nombres descriptivos
- sin espacios
- no usar palabras reservadas

```python
numero_total = 100
nombre_usuario = "Carlos"
```

---

## 📌 Resumen conceptual

| Concepto | Python |
|------|------|
| Tipado | Dinámico |
| Declaración explícita | ❌ |
| Conversión automática | ❌ |
| type() | Identifica tipo |
| Reasignación de tipo | ✅ |

---

## 🧠 Frase clave para estudiar

> "En Python no se declaran tipos, se asignan valores y el tipo lo determina el valor."

---

## 🧪 Ejemplo integrador

```python
a = 10          # int
b = 2.5         # float
c = "Python"    # str
d = True        # bool

print(type(a), type(b), type(c), type(d))
```

---

📘 Documento de apoyo académico – Programación 1

