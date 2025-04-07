# 🧠 Introducción a la Programación Orientada a Objetos (POO)

La **Programación Orientada a Objetos (POO)** es un paradigma de programación que se basa en el uso 
de "objetos", los cuales agrupan datos y funcionalidades. Es ampliamente utilizada en 
el desarrollo de software moderno debido a su capacidad de modelar estructuras 
complejas de manera más natural, organizada y reutilizable.

---

## ✅ ¿Por qué usar POO?

- **Modularidad**: permite dividir un programa en partes (clases) independientes.
- **Reutilización**: se pueden crear nuevas clases reutilizando código existente (herencia).
- **Mantenibilidad**: los programas orientados a objetos son más fáciles de entender y modificar.
- **Encapsulamiento**: protege los datos internos de los objetos para evitar cambios no deseados.
- **Abstracción**: permite enfocarse en lo esencial ignorando los detalles innecesarios.

### 🧪 Ejemplo simple de POO en Python

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

# Crear una instancia de la clase Persona
persona1 = Persona("Ana", 30)
persona1.saludar()
```

> **Salida:**
> ```
> Hola, soy Ana y tengo 30 años.
> ```

---

## ⚔️ Diferencias entre Programación Estructurada y Programación Orientada a Objetos

| Característica                        | Programación Estructurada                      | Programación Orientada a Objetos               |
|--------------------------------------|-----------------------------------------------|------------------------------------------------|
| **Enfoque**                          | En funciones y el flujo del programa           | En objetos y sus interacciones                 |
| **Organización**                     | Código dividido en funciones                  | Código dividido en clases                      |
| **Reutilización de código**          | Limitada                                      | Alta, gracias a la herencia y composición      |
| **Manejo de datos**                  | Datos globales y locales                      | Datos encapsulados dentro de objetos           |
| **Ejemplo de lenguaje típico**       | C, Pascal                                     | Python, Java, C#, C++                          |

### 🧪 Ejemplo estructurado vs orientado a objetos en Python

#### 🔹 Enfoque estructurado:
```python
def saludar(nombre, edad):
    print(f"Hola, soy {nombre} y tengo {edad} años.")

saludar("Luis", 25)
```

#### 🔹 Enfoque orientado a objetos:
```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, soy {self.nombre} y tengo {self.edad} años.")

persona = Persona("Luis", 25)
persona.saludar()
```

---

## 🎯 Conclusión

La **POO** permite construir programas más ordenados, escalables y fáciles de mantener. 
A través del uso de clases y objetos, los desarrolladores pueden representar 
entidades del mundo real en su código de forma más precisa y flexible.