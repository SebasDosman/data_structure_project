from Ordenamientos import Ordenamientos
from Menus import Menu
from CalculoSeries import CalculoSeries
from Instancias import series, nombreSeries, valoracionSeries, tempSeries, tempCap


# <-- Instancias Ordenamientos -->
ordenamiento = Ordenamientos(nombreSeries)
ordenamiento1 = Ordenamientos(tempSeries)
ordenamiento2 = Ordenamientos(tempCap)
ordenamiento3 = Ordenamientos(valoracionSeries)
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
        ordenamiento1.__bubbleSort__()
        ordenamiento2.__bubbleSort__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
        sort1 = sorted(series, key = lambda x:x.nombre)
        opcion3 = Menu.__opcionesMenuReq__()
            
        if (opcion3 == 1):
            calculoSeries.__strangerThings__(nombreSeries, sort1)
        elif (opcion3 == 2):
            sort2 = sorted(series, key = lambda x:x.cant_temp)
            sort3 = sorted(series, key = lambda x:x.cant_cap)
            calculoSeries.__tempCapMax__(tempSeries, tempCap, sort2, sort3)
        elif (opcion3 == 3):
            calculoSeries.__promedioTemp__()
        elif (opcion3 == 4):
            calculoSeries.__breakingBad__(nombreSeries, sort1)
        elif (opcion3 == 5):
            ordenamiento3.__bubbleSort__()
            sort4 = sorted(series, key = lambda x:x.valoracion)
            calculoSeries.__topCinco__(valoracionSeries, sort4)
        elif (opcion3 == 6):
            calculoSeries.__seriesMin__()
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 2):
        opcion2 = Menu.__ordenamientoSeries__()
        ordenamiento.__bubbleSortBetter__()
        ordenamiento1.__bubbleSortBetter__()
        ordenamiento2.__bubbleSortBetter__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
        sort1 = sorted(series, key = lambda x:x.nombre)
        opcion3 = Menu.__opcionesMenuReq__()
            
        if (opcion3 == 1):
            calculoSeries.__strangerThings__(nombreSeries, sort1)
        elif (opcion3 == 2):
            sort2 = sorted(series, key = lambda x:x.cant_temp)
            sort3 = sorted(series, key = lambda x:x.cant_cap)
            calculoSeries.__tempCapMax__(tempSeries, tempCap, sort2, sort3)
        elif (opcion3 == 3):
            calculoSeries.__promedioTemp__()
        elif (opcion3 == 4):
            calculoSeries.__breakingBad__(nombreSeries, sort1)
        elif (opcion3 == 5):
            ordenamiento3.__bubbleSortBetter__()
            sort4 = sorted(series, key = lambda x:x.valoracion)
            calculoSeries.__topCinco__(valoracionSeries, sort4)
        elif (opcion3 == 6):
            calculoSeries.__seriesMin__()
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 3):
        opcion2 = Menu.__ordenamientoSeries__()
        ordenamiento.__bubbleSortBidirectional__()
        ordenamiento1.__bubbleSortBidirectional__()
        ordenamiento2.__bubbleSortBidirectional__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
        sort1 = sorted(series, key = lambda x:x.nombre)
        opcion3 = Menu.__opcionesMenuReq__()
            
        if (opcion3 == 1):
            calculoSeries.__strangerThings__(nombreSeries, sort1)
        elif (opcion3 == 2):
            sort2 = sorted(series, key = lambda x:x.cant_temp)
            sort3 = sorted(series, key = lambda x:x.cant_cap)
            calculoSeries.__tempCapMax__(tempSeries, tempCap, sort2, sort3)
        elif (opcion3 == 3):
            calculoSeries.__promedioTemp__()
        elif (opcion3 == 4):
            calculoSeries.__breakingBad__(nombreSeries, sort1)
        elif (opcion3 == 5):
            ordenamiento3.__bubbleSortBidirectional__()
            sort4 = sorted(series, key = lambda x:x.valoracion)
            calculoSeries.__topCinco__(valoracionSeries, sort4)
        elif (opcion3 == 6):
            calculoSeries.__seriesMin__()
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 4):
        opcion2 = Menu.__ordenamientoSeries__()
        ordenamiento.__insertionSort__()
        ordenamiento1.__insertionSort__()
        ordenamiento2.__insertionSort__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
        sort1 = sorted(series, key = lambda x:x.nombre)
        opcion3 = Menu.__opcionesMenuReq__()
            
        if (opcion3 == 1):
            calculoSeries.__strangerThings__(nombreSeries, sort1)
        elif (opcion3 == 2):
            sort2 = sorted(series, key = lambda x:x.cant_temp)
            sort3 = sorted(series, key = lambda x:x.cant_cap)
            calculoSeries.__tempCapMax__(tempSeries, tempCap, sort2, sort3)
        elif (opcion3 == 3):
            calculoSeries.__promedioTemp__()
        elif (opcion3 == 4):
            calculoSeries.__breakingBad__(nombreSeries, sort1)
        elif (opcion3 == 5):
            ordenamiento3.__insertionSort__()
            sort4 = sorted(series, key = lambda x:x.valoracion)
            calculoSeries.__topCinco__(valoracionSeries, sort4)
        elif (opcion3 == 6):
            calculoSeries.__seriesMin__()
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 5):
        opcion2 = Menu.__ordenamientoSeries__()
        ordenamiento.__selectionSort__()
        ordenamiento1.__selectionSort__()
        ordenamiento2.__selectionSort__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
        sort1 = sorted(series, key = lambda x:x.nombre)
        opcion3 = Menu.__opcionesMenuReq__()
            
        if (opcion3 == 1):
            calculoSeries.__strangerThings__(nombreSeries, sort1)
        elif (opcion3 == 2):
            sort2 = sorted(series, key = lambda x:x.cant_temp)
            sort3 = sorted(series, key = lambda x:x.cant_cap)
            calculoSeries.__tempCapMax__(tempSeries, tempCap, sort2, sort3)
        elif (opcion3 == 3):
            calculoSeries.__promedioTemp__()
        elif (opcion3 == 4):
            calculoSeries.__breakingBad__(nombreSeries, sort1)
        elif (opcion3 == 5):
            ordenamiento3.__selectionSort__()
            sort4 = sorted(series, key = lambda x:x.valoracion)
            calculoSeries.__topCinco__(valoracionSeries, sort4)
        elif (opcion3 == 6):
            calculoSeries.__seriesMin__()
        
        opcion = Menu.__opcionesMenu__()
    elif (opcion == 6):
        opcion2 = Menu.__ordenamientoSeries__()
        ordenamiento.__shellSort__()
        ordenamiento1.__shellSort__()
        ordenamiento2.__shellSort__()
        
        if (opcion2 == 1):        
            sort = sorted(series, key = lambda x:x.genero)
            calculoSeries.__printLista__(sort)
        elif (opcion2 == 2):
            sort = sorted(series, key = lambda x:x.valoracion, reverse = True)
            calculoSeries.__printLista__(sort)
            
        sort1 = sorted(series, key = lambda x:x.nombre)
        opcion3 = Menu.__opcionesMenuReq__()
            
        if (opcion3 == 1):
            calculoSeries.__strangerThings__(nombreSeries, sort1)
        elif (opcion3 == 2):
            sort2 = sorted(series, key = lambda x:x.cant_temp)
            sort3 = sorted(series, key = lambda x:x.cant_cap)
            calculoSeries.__tempCapMax__(tempSeries, tempCap, sort2, sort3)
        elif (opcion3 == 3):
            calculoSeries.__promedioTemp__()
        elif (opcion3 == 4):
            calculoSeries.__breakingBad__(nombreSeries, sort1)
        elif (opcion3 == 5):
            ordenamiento3.__shellSort__()
            sort4 = sorted(series, key = lambda x:x.valoracion)
            calculoSeries.__topCinco__(valoracionSeries, sort4)
        elif (opcion3 == 6):
            calculoSeries.__seriesMin__()
        
        opcion = Menu.__opcionesMenu__()