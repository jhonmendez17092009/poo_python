# poo_python

- el paradicma poo esta basado en una abstracion del mundo real que nos va a permitir desarrollar programas de forma mas cercana a como vemos el mundo, pensando en objetos que tenemos delante y en acciones que podemos hacer con ellos

## clase

- una clase es un tipo de cuyas variables 
- 
atributos y metodos

### atributos 

- informacion que armacena las clasesç

### metodos

- operaciones que pueden realisar las clases 

## definicion de una clase en python

```python
class nombreclase:

    def __init__(self, variable1, variable2)
        self.atributo1 = valor1
        self.atributo2 = valor2

    def nombremetodo(self):
        bloquecodigo
```
### componentes
```class```: palabra reservada en puthon para definir una clase

```NombreClase```: nombre de la clase que quieres crear

```def```: palabra reserbada en python que se utiliza para definir tanto el constructor de la clase (metodo que e ejecuta la primera ves que usas una clase)

```__init__```: palabra reserbada en python para definir el metodo constructor de la clase. Es lo primero que se ejecuta cuando crear un objeto de una clase

```(self, variableX)```: parametro 

```self.atributoX```: forma de utilizacion y acceso a los atributos de la clase 

```nombreMetodo```: nombre del metodo de la clase

```(self)```:parametro del metodo. el parametro self es obligatorio y despues  puede tener tantos como quieras

```bloque codigo```: instruciones que ejecutara el metodo

- cuando defines una clase debes tener en cuenta los siguientes puntos:
    - puedes definir tantos atributos como nesecites
    - puedes definir tantos metodos como nesecites
    - puedes definir tantos parametros en el constructor como nesecites