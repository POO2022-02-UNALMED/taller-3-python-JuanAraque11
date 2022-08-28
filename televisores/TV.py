class TV:
    __numTV = 0

    def setNumTV(num):
        TV.__numTV = num
    def getNumTV():
        return TV.__numTV


    def __init__(self, marca, estado):
        self.__marca = marca
        self.__canal =1
        self.__precio =500
        self.__estado = estado
        self.__volumen =1
        self.__control = None
        TV.__numTV += 1

    def setMarca(self, mar):
        self.__marca = mar
    def getMarca(self):
        return self.__marca

    def setControl(self, con):
        self.__control = con
    def getControl(self):
        return self.__control

    def setPrecio(self, pre):
        self.__precio = pre
    def getPrecio(self):
        return self.__precio

    def setVolumen(self, volu):
        self.__volumen = volu
    def getVolumen(self):
        return self.__volumen

    def setCanal(self, can):
        self.__canal = can
    def getCanal(self):
        return self.__canal

    def turnOn(self):
        self.__estado = True
    def turnOff(self):
        self.__estado = False

    def getEstado(self):
        return self.__estado

    def volumenUp(self):
        if self.__estado == True and self.__volumen>=0 and self.__volumen<7:
            self.__volumen += 1
    def volumenDown(self):
        if self.__estado == True and self.__volumen>0 and self.__volumen<=7:
            self.__volumen -= 1

    def canalUp(self):
        if self.__estado == True and self.__canal>=1 and self.__canal<120:
            self.__canal += 1
    def canalDown(self):
        if self.__estado == True and self.__canal>1 and self.__canal<=120:
            self.__canal -= 1
