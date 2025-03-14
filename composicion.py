# composicion

"""una coordenada en dos dimenciones esta compuesta por dos valores, el valor en el eje de las x y el valor en el eje de las y, esta podria ser una clase.un cuadrado esta compuesto por cuatro coordenadas que son los cuatros vertises, esto podria ser una clase que esta compuesta por cuatro clases del objeto coordenada"""

# clase coordenada

class Coordenada:
    # metodo constructor
    def __init__(self, x, y):
        self.X = x
        self.Y = y
    def MostrarCoordenadas(self):
        print("(", self.X, ",", self.Y, ")")

# clase cuadrado

class Cuadrado:
    def __init__(self, v1, v2, v3, v4):
        self.V1 = v1
        self.V2 = v2
        self.V3 = v3
        self.V4 = v4

    def mostrarVertices(self):
        print("el cuadrado esta compuesto por los siguientes vertice: ")
        self.V1.MostrarCoordenadas()
        self.V2.MostrarCoordenadas()
        self.V3.MostrarCoordenadas()
        self.V4.MostrarCoordenadas()

# metodo principal
def main():
    # input
    x1 = int(input("digite el valor de x: "))
    x2 = int(input("digite el valor de y: "))

    # prosessing
    c1 = Coordenada(x1, x2)
    c1.MostrarCoordenadas()

    v1 = Coordenada(7,8)
    v2 = Coordenada(10,8)
    v3 = Coordenada(7,5)    
    v4 = Coordenada(10,5)

    cuadrado1 = Cuadrado(v1, v2, v3 ,v4)
    cuadrado1.mostrarVertices()
    
if __name__ == "__main__":
    main()

