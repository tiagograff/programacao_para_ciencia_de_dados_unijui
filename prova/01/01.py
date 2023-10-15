class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def getArea(self):
        self.area = (self.base * self.altura)
        return self.area
    
    def getPerimetro(self):
        self.perimetro = (2*(self.base + self.altura))
        return self.perimetro
    
retangulo = Retangulo(2,3)
print(retangulo.getArea())
print(retangulo.getPerimetro())