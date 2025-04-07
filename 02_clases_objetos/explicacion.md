# 🧱 Clases y Objetos en Python

En Python (y en otros lenguajes orientados a objetos), **las clases** 
son plantillas para crear objetos. Un **objeto** es una 
instancia de una clase, y representa una entidad con 
características (**atributos**) y comportamientos (**métodos**).

---

## 📦 Crear tu primera clase

Para crear una clase en Python, usamos la palabra clave `class`. 
Dentro de ella, definimos el método `__init__`, que actúa como 
constructor para inicializar los atributos del objeto.

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre  # Atributo
        self.edad = edad      # Atributo
```