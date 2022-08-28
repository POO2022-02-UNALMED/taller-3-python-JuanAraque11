class Marca:
    def __init__(self, nombre):
        self.__nombre = nombre

    def setNombre(self, nom):
        self.__nombre = nom
    def getNombre(self):
        return self.__nombre
