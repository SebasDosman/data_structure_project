from os import remove
from typing import List
from Series import Series

class CalculoSeries():
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
        print("\n \n Series: ")
        
        for i in range(0, len(list)):
            print(i + 1,".", " Nombre: ", list[i].__getNombre__(), "| Genero: ", list[i].__getGenero__(), "| Valoracion: ", list[i].__getValoracion__(), "| Cant. Temporadas: ", list[i].__getCantTemp__(), "| Cant. Capitulos: ", list[i].__getCantCap__())
        
        print("\n")
    
    def __promedioTemp__(self):
        j = 0
        
        for i in range(0, len(self.list)):
            j += self.list[i].__getCantTemp__()
            
        print("\n Cantidad de Series y Promedio de Temporadas:")
        print("Cant. Series: " , len(self.list) , "| Promedio Temporadas: ", j / len(self.list))
        print("\n")
    
    def __seriesMin__(self):
        print("\n Series con menos de 3 temporadas: ")
        
        for i in range(0, len(self.list)):
            if (self.list[i].__getCantTemp__() <= 3):
                print("Nombre: ", self.list[i].__getNombre__(), "| Cant. Temp: ", self.list[i].__getCantTemp__())
        
        print("\n")
    
    def __strangerThings__(self, list, orderList : Series):
        print("\n Serie Stranger Things: ")
        
        position = CalculoSeries.__binaria__(list, "Stranger Things")
        
        print(" Nombre: ", orderList[position].__getNombre__(), "| Genero: ", orderList[position].__getGenero__(), "| Valoracion: ", orderList[position].__getValoracion__(), "| Cant. Temporadas: ", orderList[position].__getCantTemp__(), "| Cant. Capitulos: ", orderList[position].__getCantCap__())
        print("\n")
    
    def __breakingBad__(self, list, orderList : Series):
        position = CalculoSeries.__binaria__(list, "Breaking Bad")
        cantCap = orderList[position].__getCantCap__()
        cantTemp = orderList[position].__getCantTemp__()
        prom = cantCap / cantTemp
        print("\n Promedio de Capitulos por Temporada de la serie Breaking Bad: ")
        print("Cant. Cap: " , cantCap , "| Cant. Temp: " , cantTemp , "| Promedio: " , prom)
        print("\n")
    
    def __tempCapMax__(self, listTemp, listCap, orderListTemp : Series, orderListCap : Series):
        positionTemp = CalculoSeries.__binaria__(listTemp, max(listTemp))
        print("\n Serie con mayor Cant. Temporadas: ")
        print(" Nombre: ", orderListTemp[positionTemp].__getNombre__(), "| Genero: ", orderListTemp[positionTemp].__getGenero__(), "| Valoracion: ", orderListTemp[positionTemp].__getValoracion__(), "| Cant. Temporadas: ", orderListTemp[positionTemp].__getCantTemp__(), "| Cant. Capitulos: ", orderListTemp[positionTemp].__getCantCap__())
        
        positionCap = CalculoSeries.__binaria__(listCap, max(listCap))
        print("Serie con mayor Cant. Capitulos: ")
        print(" Nombre: ", orderListCap[positionCap].__getNombre__(), "| Genero: ", orderListCap[positionCap].__getGenero__(), "| Valoracion: ", orderListCap[positionCap].__getValoracion__(), "| Cant. Temporadas: ", orderListCap[positionCap].__getCantTemp__(), "| Cant. Capitulos: ", orderListCap[positionCap].__getCantCap__())
        print("\n")
    
    def __topCinco__(self, listValoracion : List, orderList : List):
        listResul : Series = []
        
        while (len(listResul) < 5):
            maximum = CalculoSeries.__binaria__(listValoracion, max(listValoracion))
            listValoracion.pop(maximum)
            listResul.append(orderList[maximum])
            orderList.pop(maximum)
        
        self.__printLista__(listResul)
    
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