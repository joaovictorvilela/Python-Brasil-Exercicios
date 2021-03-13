class Tv(object):
    def __init__(self, numeroDoCanal, volume = 0):
        self.__numeroDoCanal = numeroDoCanal
        self.__volume = volume

    def AumentarVolume(self, valor):
        if (self.__volume <= 100):
            self.__volume += 1

    def DiminuiVolume(self):
        if (self.__volume > 0):
            self.__volume -= 1

    def MudarCanal(self, numero):
        self.__numeroDoCanal = numero
