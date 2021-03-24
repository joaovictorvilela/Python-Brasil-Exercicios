class Tv(object):
    def __init__(self, numeroDoCanal, volume = 0):
        self.numeroDoCanal = numeroDoCanal
        self.volume = volume

    def AumentarVolume(self, valor):
        if (self.volume <= 100):
            self.volume += 1

    def DiminuiVolume(self):
        if (self.volume > 0):
            self.volume -= 1

    def MudarCanal(self, numero):
        self.numeroDoCanal = numero
