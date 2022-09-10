from Ordenamientos import Ordenamientos
from Menus import Menu
from CalculoSeries import CalculoSeries
from Instancias import series, nombreSeries, generoSeries, valoracionSeries, tempSeries, tempCap



# <-- Instancias Ordenamientos -->
ordenamiento = Ordenamientos(nombreSeries)
calculoSeries = CalculoSeries(series)



# <-- Mensajes -->
Menu.__bienvenida__()
calculoSeries.__printSeries__()
opcion = Menu.__opcionesMenu__()



# <-- Menu -->
while (opcion != -1):
    if (opcion == 1):
        opcion2 = Menu.__ordenamientoSeries__()
        ordenamiento.__bubbleSort__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                calculoSeries.__promedioTemp__()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion3 == 6):
                calculoSeries.__seriesMin__()
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                calculoSeries.__promedioTemp__()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion3 == 6):
                calculoSeries.__seriesMin__()
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 2):
        opcion2 = Menu.__ordenamientoSeries__()
        ordenamiento.__bubbleSortBetter__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                calculoSeries.__promedioTemp__()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion3 == 6):
                calculoSeries.__seriesMin__()
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                calculoSeries.__promedioTemp__()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion3 == 6):
                calculoSeries.__seriesMin__()
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 3):
        opcion2 = Menu.__ordenamientoSeries__()
        ordenamiento.__bubbleSortBidirectional__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                calculoSeries.__promedioTemp__()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion3 == 6):
                calculoSeries.__seriesMin__()
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                calculoSeries.__promedioTemp__()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion3 == 6):
                calculoSeries.__seriesMin__()
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 4):
        opcion2 = Menu.__ordenamientoSeries__()
        ordenamiento.__insertionSort__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                calculoSeries.__promedioTemp__()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion3 == 6):
                calculoSeries.__seriesMin__()
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                calculoSeries.__promedioTemp__()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion3 == 6):
                calculoSeries.__seriesMin__()
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 5):
        opcion2 = Menu.__ordenamientoSeries__()
        ordenamiento.__selectionSort__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                calculoSeries.__promedioTemp__()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion3 == 6):
                calculoSeries.__seriesMin__()
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                calculoSeries.__promedioTemp__()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion3 == 6):
                calculoSeries.__seriesMin__()
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 6):
        opcion2 = Menu.__ordenamientoSeries__()
        ordenamiento.__shellSort__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                calculoSeries.__promedioTemp__()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion3 == 6):
                calculoSeries.__seriesMin__()
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
            opcion3 = Menu.__opcionesMenuReq__()
            
            if (opcion3 == 1):
                sort1 = sorted(series, key = lambda x:x.nombre)
                calculoSeries.__strangerThings__(nombreSeries, sort1)
            elif (opcion3 == 2):
                print()
            elif (opcion3 == 3):
                calculoSeries.__promedioTemp__()
            elif (opcion3 == 4):
                print()
            elif (opcion3 == 5):
                print()
            elif (opcion3 == 6):
                calculoSeries.__seriesMin__()
        
        opcion = Menu.__opcionesMenu__()