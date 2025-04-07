class Persona():
    def __init__(self, nombre, edad, nacionalidad):
        self.nombre = nombre
        self.edad = edad
        self.nacionalidad = nacionalidad
        
    def hablar(self):
        print("Hablando...")
        
    def informacion(self):
        print(self.nombre, self.edad, self.nacionalidad)
        
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
        return f"{super().informacion_profesion()}" 

persona_profesional = PersonaProfesional("Luis", 22, "Español", "Ingeniero", "Sicsa")
persona_profesional.presentarse()

herencia = issubclass(PersonaProfesional, Persona)
print(herencia)