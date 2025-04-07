class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hablando...")
        
    def informacion(self):
        print(self.nombre, self.edad, self.nacionalidad)

### Heredad Metodos y Atributos ###
# De esta manera podemos heredar tanto atributos como metodos, 
# pero no podemos agregar nuevos que no sean propios de la 
# clase padre
class Empleado(Persona):
    pass

### Heredacion y nuevos atributos y metodos ###
# Para poder heredar y agregar atributos o metodos nuevos, se usa
# la función super()
class Tutor(Persona): # Podemos pasar por argumento la clase padre
    def __init__(self, nombre, edad, nacionalidad, cargo):
        super().__init__(nombre, edad, nacionalidad) # hereda de persona las propiedades especificadas en el argumento
        self.cargo = cargo # atributo único
        
    def informacion_cargo(self):
        print(self.cargo)
        
### Herencia multiple ###
class Profesional():
    def __init__(self, profesion):
        self.profesion = profesion
        
    def informacion_profesion(self):
        print(self.profesion)

class PersonaProfesional(Persona, Profesional):
    def __init__(self, nombre, edad, nacionalidad, profesion, empresa):
        Persona.__init__(self, nombre, edad, nacionalidad)
        Profesional.__init__(self, profesion)
        self.empresa = empresa
        
    def presentarse(self):
        return f"{super().informacion_profesion()}" # Acceder al metodo de la clase padre
        #return f"{self.informacion_profesion()}" # Acceder al metodo de la clase actual (asi misma, self)

      
"""persona = Persona("Luis", 22, "Español")    
persona1 = Tutor("Luis", 22, "Español", "Inspector")

persona1.hablar()
print(persona.nombre)
print(persona1.cargo)"""

persona_profesional = PersonaProfesional("Luis", 22, "Español", "Ingeniero", "Sicsa")
persona_profesional.presentarse()

# determinar si es una subclase que hereda cierta clase
herencia = issubclass(PersonaProfesional, Tutor)
print(herencia)