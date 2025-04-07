### Creemos nuestra primera clase ###
class Persona():
    # el metodo init actua como nuestro constructor para inicializar atributos de nuestro objeto
    def __init__(self, nombre, apellido, edad): # el argumento self es obligatorio, se refiere "asi mismo"
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        # Las variables con self. son los atributos de la clase, son "asi mismo _atributo_"
        
### Instanciemos objetos ###

persona1 = Persona("Gabo", "Mendieta", 18) # Aqui ya estamos instanciando la clase, se convierte en objeto

print(persona1) # Imprime la direccion de memoria del objeto

print(persona1.edad) # Accedemos a la edad de persona1 y la imprime

"""
Diferenciemos los métodos con las funciones.
- Los métodos son aquellos que realizan un proceso pero no retornan un valor

- Las funciones a diferencia de los métodos retornan valores
"""