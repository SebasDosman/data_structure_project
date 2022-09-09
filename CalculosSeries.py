from Series import Series

class CalculosSeries():
    list : Series = []
    
    def __init__(self, list : Series):
        self.list = list
    
    def __getList__(self):
        return self.list
    
    def __setList__(self, list):
        self.list = list
    
    def __printSeries__(self):
        print("Series Disponibles: ")
        
        for i in range(0, len(self.list)):
            print(i + 1,".", " Nombre: ", self.list[i].__getNombre__(), "| Genero: ", self.list[i].__getGenero__(), "| Valoracion: ", self.list[i].__getValoracion__(), "| Cant. Temporadas: ", self.list[i].__getCantTemp__(), "| Cant. Capitulos: ", self.list[i].__getCantCap__())
        
        print("\n")
    
    def __promedioTemp__(self):
        j = 0
        
        for i in range(0, len(self.list)):
            j += self.list[i].__getCantTemp__()
            
        print("Promedio Temporadas: ", j / len(self.list))
        print("\n")
    
    def __seriesMin__(self):
        print("Series con menos de 3 temporadas: ")
        
        for i in range(0, len(self.list)):
            if (self.list[i].__getCantTemp__() <= 3):
                print(self.list[i].__getNombre__())
        
        print("\n")