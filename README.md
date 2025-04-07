<div align="center">
  <img src="https://facialix.com/wp-content/uploads/2022/06/python-poo-facialix.jpg" height="400" alt="poo, facialix"  />
</div>

# 📘 Módulo de Programación Orientada a Objetos (POO) con Python

Este repositorio está dedicado al aprendizaje de la **Programación 
Orientada a Objetos (POO)** utilizando el lenguaje **Python** desde un 
nivel completamente principiante.

---

## 🧠 ¿Qué es la POO?

La **Programación Orientada a Objetos** es un paradigma de programación que utiliza *objetos* y *clases* para organizar el código de manera más estructurada, reutilizable y mantenible.

En lugar de escribir funciones sueltas, la POO agrupa datos (atributos) y comportamientos (métodos) dentro de estructuras llamadas **clases**.

---

## 🚀 ¿Qué necesitas para empezar?

- Conocimientos básicos de Python: variables, funciones, listas, condicionales.
- Un editor de código (como VSCode, PyCharm o incluso IDLE).
- Muchas ganas de aprender ✨.

---

## 📚 Temas Cubiertos

1. **Introducción a la POO**
   - ¿Por qué usar POO?
   - Diferencias entre programación estructurada y orientada a objetos

2. **Clases y Objetos**
   - Crear tu primera clase
   - Instanciar objetos
   - Atributos y métodos

3. **Constructores (`__init__`)**
   - Inicialización de atributos

4. **Encapsulamiento**
   - Públicos, protegidos y privados
   - Uso de getters y setters

5. **Herencia**
   - Crear clases hijas
   - Reutilización de código

6. **Polimorfismo**
   - Métodos sobrescritos
   - Uso de `super()`

7. **Abstracción**
   - Ocultar la complejidad
   - Clases abstractas (con `abc`)

8. **Ejercicios prácticos**
   - Simulación de una tienda
   - Sistema de gestión de estudiantes
   - Juego simple orientado a objetos

---

## 💡 Ejemplo Simple

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

persona1 = Persona("Ana", 25)
persona1.saludar()
