from Series import Series

class CalculosSeries():
    list : Series = []
    
    def __init__(self, list):
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
    
    def __printLista__(self, list):
        print("\n \n Series Disponibles: ")
        
        for i in range(0, len(list)):
            print(i + 1,".", " Nombre: ", list[i].__getNombre__(), "| Genero: ", list[i].__getGenero__(), "| Valoracion: ", list[i].__getValoracion__(), "| Cant. Temporadas: ", list[i].__getCantTemp__(), "| Cant. Capitulos: ", list[i].__getCantCap__())
        
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
                print("Nombre: ", self.list[i].__getNombre__(), "| Cant. Temp: ", self.list[i].__getCantTemp__())
        
        print("\n")
    
    def __strangerThings__(self, list, orderList : Series):
        print("\n Serie Stranger Things: ")
        position = CalculosSeries.__binaria__(list, "Stranger Things")
        print(" Nombre: ", orderList[position].__getNombre__(), "| Genero: ", orderList[position].__getGenero__(), "| Valoracion: ", orderList[position].__getValoracion__(), "| Cant. Temporadas: ", orderList[position].__getCantTemp__(), "| Cant. Capitulos: ", orderList[position].__getCantCap__())
        print("\n")
    
    def __binaria__(list, found):
        position = -1
        first = 0
        last = len(list) - 1
        
        while (first <= last) and (position == -1):
            middle = (first + last) // 2
            
            if (list[middle] == found):
                position = middle
            else:
                if (found < list[middle]):
                    last = middle - 1
                else: 
                    first = middle + 1
        return position