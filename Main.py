from Series import Series
from Ordenamientos import Ordenamientos
from Menus import Menu
from CalculosSeries import CalculosSeries



# <-- Instancias De Clases : Series Disponibles -->
strangerThings = Series("Stranger Things", "Accion", 4.5, 3, 5)
lucifer = Series("Lucifer", "Comedia", 3, 4, 3)
breakingBad = Series("Breaking Bad", "Ficcion", 4, 9, 64)
bettyLaFea = Series("Betty La Fea", "Romance", 2.5, 6, 10)
bobEsponja = Series("Bob Esponja", "Cartoon", 5, 4, 8)
sandMan = Series("Sand Man", "Comedia", 2.5, 6, 2)



# <-- Listas de Atributos -->
series = [strangerThings, lucifer, breakingBad, bettyLaFea, bobEsponja, sandMan]
nombreSeries = [strangerThings.__getNombre__(), lucifer.__getNombre__(), breakingBad.__getNombre__(), bettyLaFea.__getNombre__(), bobEsponja.__getNombre__(), sandMan.__getNombre__()]
generoSeries = [strangerThings.__getGenero__() , lucifer.__getGenero__(), breakingBad.__getGenero__(), bettyLaFea.__getGenero__(), bobEsponja.__getGenero__(), sandMan.__getGenero__()]
valoracionSeries = [strangerThings.__getValoracion__(), lucifer.__getValoracion__(), breakingBad.__getValoracion__(), bettyLaFea.__getValoracion__(), bobEsponja.__getValoracion__(), sandMan.__getValoracion__()]
tempSeries = [strangerThings.__getCantTemp__(), lucifer.__getCantTemp__(), breakingBad.__getCantTemp__(), bettyLaFea.__getCantTemp__(), bobEsponja.__getCantTemp__(), sandMan.__getCantTemp__()]
tempSeries = [strangerThings.__getCantCap__(), lucifer.__getCantCap__(), breakingBad.__getCantCap__(), bettyLaFea.__getCantCap__(), bobEsponja.__getCantCap__(), sandMan.__getCantCap__()]



# <-- Instancias Ordenamientos -->
ordenamiento = Ordenamientos(nombreSeries)
calculoSeries = CalculosSeries(series)



Menu.__bienvenida__()
calculoSeries.__printSeries__()
opcion = Menu.__opcionesMenu__()



# <-- Menu Requerimientos -->
# calculoSeries.__promedioTemp__()
# calculoSeries.__seriesMin__()



# <-- Menu -->
while (opcion != -1):
    if (opcion == 1):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                ordenamiento.__bubbleSort__()
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                print()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion == 6):
                print()
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                ordenamiento.__bubbleSort__()
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                print()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion == 6):
                print()
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 2):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                ordenamiento.__bubbleSortBetter__()
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                print()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion == 6):
                print()
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                ordenamiento.__bubbleSortBetter__()
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                print()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion == 6):
                print()
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 3):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                ordenamiento.__bubbleSortBidirectional__()
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                print()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion == 6):
                print()
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                ordenamiento.__bubbleSortBidirectional__()
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                print()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion == 6):
                print()
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 4):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                ordenamiento.__insertionSort__()
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                print()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion == 6):
                print()
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                ordenamiento.__insertionSort__()
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                print()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion == 6):
                print()
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 5):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                ordenamiento.__selectionSort__()
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                print()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion == 6):
                print()
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                ordenamiento.__selectionSort__()
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                print()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion == 6):
                print()
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 6):
        opcion2 = Menu.__ordenamientoSeries__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                ordenamiento.__shellSort__()
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                print()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion == 6):
                print()
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                ordenamiento.__shellSort__()
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                print()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion == 6):
                print()
        
        opcion = Menu.__opcionesMenu__()