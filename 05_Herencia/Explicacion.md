# 🧬 Herencia en Programación Orientada a Objetos (POO)

## 📌 ¿Qué es la Herencia?

La **herencia** es uno de los principios fundamentales de la 
**programación orientada a objetos (POO)**. Consiste en la 
capacidad de una clase (denominada **subclase** o **clase hija**) 
de **heredar atributos y métodos** de otra clase (conocida como 
**superclase** o **clase padre**).

Esto permite **reutilizar código**, mantenerlo más organizado y 
facilitar la **extensibilidad** del sistema.

---

## 🧱 Sintaxis básica en Python

```python
# Clase padre
class Animal:
    def comer(self):
        print("El animal está comiendo.")

# Clase hija
class Perro(Animal):
    def ladrar(self):
        print("El perro está ladrando.")

# Uso
mi_perro = Perro()
mi_perro.comer()   # Método heredado
mi_perro.ladrar()  # Método propio
