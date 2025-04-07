# 🧠 Method Resolution Order (MRO) en Python

## ¿Qué es el MRO?

El **MRO (Method Resolution Order)** es el **orden en que Python 
busca métodos y atributos** cuando los llamas desde una 
instancia de clase, especialmente cuando estás trabajando con 
**herencia múltiple**.

Python necesita una forma lógica de decidir **de qué clase tomar 
el método** si varias clases lo tienen.

---

## 🧪 Ejemplo básico con supper()

```python
class A:
    def accion(self):
        print("A")

class B(A):
    def accion(self):
        print("B")
        super().accion()

class C(A):
    def accion(self):
        print("C")
        super().accion()

class D(B, C):
    def accion(self):
        print("D")
        super().accion()

d = D()
d.accion()

# Salida:
"""
D
B
C
A
"""
```
super() sigue el orden de D → B → C → A → object.
