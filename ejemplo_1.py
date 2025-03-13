# Clase personas 

class persona:
    # metodo constructor
    def __init__(self, nombre, apellidos, edad):
        self.Nombre = nombre
        self.Apellidos = apellidos
        self.Edad = edad
def MostrarPersona(self):
    print("Nombre: " + self.Nombre)
    print("Apellido: " + self.Apellidos)
    print("Edad: " + str (self.Edad))

def main():
    p1 = persona("Jhoasnel", "Mendez", 15)
    p1.MostrarPersona()
    p2 = persona("Nestor", "Paez", 25)
    p2.MostrarPersona()
    p1.Edad = 18
    p1.MostrarPersona()
    p1 = p2
    p1.MostrarPersona()
    p2.MostrarPersona()

if __name__ == "__main__":
    main()